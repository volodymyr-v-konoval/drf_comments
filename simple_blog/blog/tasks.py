import os
from celery import shared_task
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from .models import Comment


es_client = Elasticsearch(
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
        es_client.index(index="comments", id=comment.id, body={
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

        es_client.index(index="comments", 
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
    try:
        es_client.delete(index="comments", id=comment_id)
        print(f"Comment {comment_id} was deleted from Elasticsearch")
    except NotFoundError:
        print(f"Comment {comment_id} not found in Elasticsearch – nothing to delete.")
    except Exception as e:
        print(f"Error deleting comment from Elasticsearch: {e}")
            