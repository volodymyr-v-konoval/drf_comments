import os
from celery import shared_task
from elasticsearch import Elasticsearch
from .models import Comment


es = Elasticsearch(
    [os.getenv("OPENSEARCH_HOSTS")],
    basic_auth=(
        os.getenv("OPENSEARCH_USER"),
        os.getenv("OPENSEARCH_PASSWORD")
    ),
    headers={"User-Agent": "opensearch-py"},
    request_timeout=30,
    verify_certs=False
)



@shared_task
def index_comment(comment_id):

    try:
        comment = Comment.objects.get(id=comment_id)
        username = comment.username.username
        created = comment.created.isoformat()
        es.index(index="comments", id=comment.id, body={
            "username": username,
            "text": comment.text,
            "created": created
            }
        )
    except Comment.DoesNotExist:
        print(f"Comment with ID {comment_id} does not exists.")


@shared_task
def update_comment_in_elasticsearch(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        username = comment.username.username
        created = comment.created.isoformat()

        es.index(index="comments", 
                id=comment.id, 
                body={
                    "username": username, 
                    "text": comment.text,
                    "created": created
                })
    except Comment.DoesNotExist:
        print(f"Comment with ID {comment_id} does not exists.")
    
@shared_task
def delete_comment_from_elasticsearch(comment_id):
    es.delete(id=comment_id)
    print(f"Comment {comment_id} was deleted from Elasticsearch")
