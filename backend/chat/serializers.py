from rest_framework import serializers
from .models import ChatRoom, ChatMessage
from accountdata.serializers import AppUserSerializer

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('id', 'room', 'message')
        read_only_fields = ('id',)

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = AppUserSerializer(many=True)
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ('id', 'participants', 'created_at', 'messages')
        read_only_fields = ('id', 'created_at')