from celery import shared_task
from elasticsearch import Elasticsearch
from .models import Comment


es = Elasticsearch(["http://localhost:9200"],
                   basic_auth=("elastic", "EusuO9toKtg6zBT02yZ5"))



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
    es.delete(index="comments", id=comment_id)
    print(f"Comment {comment_id} was deleted from Elasticsearch")
