from rest_framework import viewsets,generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import UserSerializer, FriendSerializer, ChatMessageSerializer
from .models import User, Friend, ChatMessage



# @api_view(['GET'])
class ProfiletViewSet(viewsets.ModelViewSet):# generics.GenericAPIView
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
   
  

#@api_view(['POST'])
class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# def create_friend(request):
#     data = request.data
#     serializer =ChatSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
