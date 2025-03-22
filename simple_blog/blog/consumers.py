import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("comments", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("comments", self.channel_name)

    async def new_comment(self, event):
        comment_data = event["comment"]
        await self.send(text_data=json.dumps(comment_data))