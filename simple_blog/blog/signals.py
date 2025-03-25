from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from blog.models import Comment
from blog.documents import CommentDocument
from opensearchpy.helpers import BulkIndexError

@receiver(post_save, sender=Comment)
def update_comment_in_index(sender, instance, **kwargs):
    CommentDocument().update(instance, action='index') 

@receiver(post_delete, sender=Comment)
def delete_comment_from_index(sender, instance, **kwargs):
    try:
        CommentDocument().update(instance, action='delete', refresh=True)
    except BulkIndexError as e:
        errors = e.errors if hasattr(e, 'errors') else []
        if all(err.get('delete', {}).get('status') == 404 for err in errors):
            print(f"[INFO] Comment {instance.id} not found in OpenSearch index — skipping delete.")
        else:
            raise e 
        