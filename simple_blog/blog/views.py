from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Comment
from .serializers import CommentSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save()
        data = CommentSerializer(comment).data
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "comments",
            {
                "type": "new_comment",
                "comment": data
            }
        )


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
