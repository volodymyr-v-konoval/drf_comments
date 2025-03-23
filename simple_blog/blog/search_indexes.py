from elasticsearch_dsl import Document, Text, Date
from django_elasticsearch_dsl.registries import registry
from .models import Comment


@registry.register_document
class CommentDocument(Document):
    userame = Text()
    text = Text()
    created_at = Date()

    class Index:
        name = "comments"
        