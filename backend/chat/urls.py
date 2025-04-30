from django.urls import path
from .views import ChatRoomListView, CreateChatRoomView, MessageListView, SendMessageView

urlpatterns = [
    path("", ChatRoomListView.as_view(), name="chat-list"),
    path("create/", CreateChatRoomView.as_view(), name="create-chat-room"),
    path("<int:room_id>/", MessageListView.as_view(), name="chat-messages"),
    path("<int:room_id>/send/", SendMessageView.as_view(), name="send-message"),
]
