from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Comment
from .serializers import CommentSerializer, UserSerializer
from elasticsearch import Elasticsearch
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.tasks import (index_comment,
                        update_comment_in_elasticsearch,
                        delete_comment_from_elasticsearch)


es = Elasticsearch(["http://localhost:9200"])


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

    def perform_update(self, serializer):
        comment = serializer.save()
        update_comment_in_elasticsearch.delay(comment.id)

    def perform_destroy(self, instance):
        delete_comment_from_elasticsearch.delay(instance.id)
        instance.delete()


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


@api_view(["GET"])
def search_comments(request):
    query = request.GET.get("q", "")
    response = es.search(index="comments", 
                         body={
                             "query": {"match": {"text": query}}
                             }
                            )
    return Response(response["hits"]["hits"])
