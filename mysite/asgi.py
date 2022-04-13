
# mysite/asgi.py
# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import chat.routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })

import os
# from . import consumers

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
            # url(r"^chat/$", PublicChatConsumer.as_asgi()),
        ])
    ),
})