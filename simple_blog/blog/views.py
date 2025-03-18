from rest_framework import viewsets, permissions
# from rest_framework.pagination import PageNumberPagination
from .models import Comment
from .serializers import CommentSerializer

# class CustomPaginationExample(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 25


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = CustomPaginationExample

