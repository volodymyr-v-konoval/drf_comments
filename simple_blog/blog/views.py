from rest_framework import viewsets, permissions, generics
from .models import Comment
from .serializers import CommentSerializer, UserSerializer



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
