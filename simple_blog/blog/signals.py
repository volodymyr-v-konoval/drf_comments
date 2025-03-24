from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from blog.models import Comment
from blog.documents import CommentDocument

@receiver(post_save, sender=Comment)
def update_comment_in_index(sender, instance, **kwargs):
    CommentDocument().update(instance, action='index') 

@receiver(post_delete, sender=Comment)
def delete_comment_from_index(sender, instance, **kwargs):
    CommentDocument().delete(instance, ignore=404)  
    