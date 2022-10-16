from django.contrib import admin
from .models import ChatMessage, Friend, User

# Register your models here.
#admin.site.register(User)
admin.site.register(Friend)
admin.site.register(ChatMessage)