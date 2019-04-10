
from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner
        print("printing inner ======>",inner,type(inner))

    def __call__(self, scope):
        
        print("printing scope======>",scope)
        try:
            query_string=scope['query_string'].decode().split('=')
            if len(query_string)==1:
                custom_is_authenticated=False
            elif len(query_string)>2:
                custom_is_authenticated=False
            else:
                custom_is_authenticated=True
        except Exception as e:
            custom_is_authenticated=False

                

        
        close_old_connections()
        scope['custom_is_authenticated'] = custom_is_authenticated
        
        
        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))