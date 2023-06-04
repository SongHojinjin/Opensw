
from django.shortcuts import render


def index(request): # index 템플릿 렌더링
    return render(request, "chat/index.html")


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from post import Post

@login_required
def create_room(request):
    # 새로운 채팅방 생성
    chat_room = ChatRoom.objects.create()
    chat_room.participants.add(request.user)
    # 채팅방으로 리디렉션
    return redirect('room', room_id=chat_room.id) #room_id는 채팅방의 url주소

@login_required
class JoinChatRoomAPIView(APIView): # receiveuser 채팅방 참여
    def post(self, request, post_id, format=None):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.recieveuser:
            post.chatroom.participants.add(request.user)
            return Response({'message': 'Successfully joined the chat room.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You are not allowed to join this chat room.'}, status=status.HTTP_403_FORBIDDEN)

@login_required
def room(request, room_id): # 참여된 채팅방이라면 입장
    print(room_id)
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    
    # 채팅방에 속해 있는지 확인하는 로직을 구현
    if request.user in chat_room.participants.all():
        print('승인')
        return render(request, "chat/room.html", {"room_id": room_id,'realname':request.user.realname})
    else:
        print('거절')
        return render(request, "chat/access_denied.html")



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatRoom
from .serializers import ChatRoomSerializer

# 현재 로그인한 사용자의 채팅방 조회
"""class ChatRoomListAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.user.id
        chat_rooms = ChatRoom.objects.filter(participants__id=user_id)
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """
# 모든 채팅방 조회
class ChatRoomListAPIView(APIView):
    def get(self, request, format=None):
        chat_rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)