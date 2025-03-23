from django.core.management.base import BaseCommand
from blog.models import Comment
from blog.tasks import index_comment


class Command(BaseCommand):
    help = "Rebuilding the search index for all commens!"

    def handle(self, *args, **kwargs):
        for comment in Comment.objects.all():
            index_comment.delay(comment.id)
