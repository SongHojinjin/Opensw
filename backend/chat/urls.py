from django.urls import path

from . import views
from .views import ChatRoomListAPIView

urlpatterns = [
    path("", views.index, name="index"), # index
    path("room/<int:room_id>/", views.room, name = 'room'), # 채팅방
    path('see/rooms/', ChatRoomListAPIView.as_view(), name='chat-room-list'), #채팅방 리스트
]