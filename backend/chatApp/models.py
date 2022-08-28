import profile
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here. for user chat 

class User(User):
    #phone_number=PhoneNumberField(unique=True,null=False,blank=False)
    #date_joined=models.DateTimeField(_('Date'),auto_now_add=True)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends",blank=True, null=True)


    REQUIRED_FIELDS=['username','email']
    USERNAME_FIELD='email'

    def __str__(self):
        return f"User: {self.username}"

    
    
class Friend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Friend: { self.user.username }"

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body