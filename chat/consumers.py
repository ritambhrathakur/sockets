import json
from channels.generic.websocket import WebsocketConsumer
from .models import ChatMessages

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("869y8oak,js")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        x1=ChatMessages.objects.filter(text_name=self.room_name)
        # print(x1)
      
        self.accept()
        for i in x1:
            self.send(text_data=json.dumps({
                'message': i.message

            }))

    def disconnect(self, close_code):
        print("socket dis1234")
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        x1=self.save_messages(self.scope,message)
        if x1 is True:
            print('message has been saved')
        print('--------------------------------->> Recieve')
        

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
        print('--------------------------------->> Chat Message')
        
        
    def save_messages(self,scope,event):
        print(event)
        res1=ChatMessages()
        res1.text_name=scope["url_route"]["kwargs"]["room_name"]
        res1.message=event
        res1.save()
        return True