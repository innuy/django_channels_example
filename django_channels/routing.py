from channels.routing import route
from django_channels_app.consumers import message_ws, listener_add, listener_discconect

WEBSOCKET_RECEIVE = "websocket.receive"
WEBSOCKET_DISCONNECT = "websocket.disconnect"
WEBSOCKET_CONNECT = "websocket.connect"

channel_routing = [
    route(WEBSOCKET_RECEIVE, message_ws),
    route(WEBSOCKET_DISCONNECT, listener_discconect),
    route(WEBSOCKET_CONNECT, listener_add),
]
