from django.contrib import admin
from .models import ChatMessage, Friend, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(ChatMessage)