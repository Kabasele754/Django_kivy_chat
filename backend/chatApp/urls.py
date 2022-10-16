from django.urls import path, re_path, include
#from django.conf.urls import patterns, include, url
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
]