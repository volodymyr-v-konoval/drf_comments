import logging
import os
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.cache import cache
from elasticsearch import Elasticsearch
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.tasks import (index_comment,
                        update_comment_in_elasticsearch,
                        delete_comment_from_elasticsearch)
from .serializers import CommentSerializer, UserSerializer
from .models import Comment


logger = logging.getLogger("events")


es = Elasticsearch(
    [os.getenv("OPENSEARCH_HOSTS")],
    basic_auth=(
        os.getenv("OPENSEARCH_USER"),
        os.getenv("OPENSEARCH_PASSWORD")
    ),
    headers={"User-Agent": "opensearch-py"},
    request_timeout=30,
    verify_certs=False
)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        cache_key = "comments_list"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)
        
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=300)
        return response

    def perform_create(self, serializer):
        comment = serializer.save()
        index_comment.delay(comment.id)
        data = CommentSerializer(comment).data
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "comments",
            {
                "type": "new_comment",
                "comment": data
            }
        )
        cache.delete("comments_list")
        logger.info(f"Comment {comment.id} was created by {comment.username}")

    def perform_update(self, serializer):
        comment = serializer.save()
        update_comment_in_elasticsearch.delay(comment.id)
        cache.delete("comments_list")

        logging.info(f"Comment {comment.id} was updated by user {comment.username}")
        
    def perform_destroy(self, instance):
        print(f"[DEBUG] Deleting object: {instance} of type {type(instance)}")  
        delete_comment_from_elasticsearch.delay(instance.id)
        instance.delete()
        cache.delete("comments_list")

        logger.info(f"Comment {instance.id} wsa deleted by {instance.username}")


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


@api_view(["GET"])
def search_comments(request):
    query = request.GET.get("q", "")
    cache_key = f"search:{query}"
    cached_results = cache.get(cache_key)

    if cached_results:
        return Response(cached_results)
    
    response = es.search(index="comments", 
                         body={
                             "query": {"match": {"text": query}}
                             }
                            )
    results = response["hits"]["hits"]

    cache.set(cache_key, results, timeout=600)
    return Response(results)
