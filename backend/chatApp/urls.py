from django.urls import path, re_path, include
#from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profile', views.ProfiletViewSet)
router.register(r'friend', views.FriendViewSet)
router.register(r'message', views.ChatMessageViewSet)

urlpatterns = [
    #path('', views.all_friend, name='all_friend'),
    #path('create', views.create_friend, name='create_friend')
    path('api/', include(router.urls)),
    path('api_prifil', views.ProfileList.as_view()),
    path('api_friend', views.FriendList.as_view()),
    path('api_message_detail/<int:pk>/', views.MessageDetail.as_view()),
    path('api_chat_detail/<int:pk>/', views.ChatMessageDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)