from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import ProfilSerializer, FriendSerializer, ChatMessageSerializer
from .models import Profile, Friend, ChatMessage


# @api_view(['GET'])
class ProfiletViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
    
class ProfileList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
  
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
  
class ProfileDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
  
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
  
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  
  

#@api_view(['POST'])
class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
# def create_friend(request):
#     data = request.data
#     serializer =ChatSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

class FriendList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
  
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProfileDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
  
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
  
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  
  



class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
