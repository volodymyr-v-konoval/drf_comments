from django.conf import settings
from django.db import models

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return (
#             super().get_queryset().filter(status=Post.Status.PUBLISHED)
#         )


class Comment(models.Model):

    username = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='comments')
    email = models.EmailField()
    homepage = models.URLField(blank=True)
    text = models.CharField(max_length=2500) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', 
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True, 
                               related_name='replies')


    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Comment by {self.username} on {self.created}'
