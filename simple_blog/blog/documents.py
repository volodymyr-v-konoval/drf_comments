from django_opensearch_dsl.registries import registry
from django_opensearch_dsl.documents import Document
from opensearchpy import Text, Date
from .models import Comment

@registry.register_document
class CommentDocument(Document):
    class Index:
        name = "comments"

    class Django:
        model = Comment
        fields = ["text", "created"]
