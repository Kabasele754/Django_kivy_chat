from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField



# # Model Person
# class Person(User): 
#     birth_date = models.DateField()
#     phone = models.CharField(max_length=15)
#     type_user = models.CharField(max_length=50, default="client")
# pip install django-phonenumber-field
    
    # def __str__(self) -> str:
    #     return self.first_name

    # @property
    # def full_name(self):
    #     "Returns the person's full name."
    #     return '%s %s' % (self.first_name, self.last_name)
    
    # class Meta:
    #     ordering = ["last_name", "first_name","birth_date","phone","email","type_user"]

# Model Abstract Room and Blog



class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True, help_text='Must be in format +(243)9999999999') 
    photo = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends",blank=True, null=True)
    # pip install django-phonenumber-field
    #pip install django-phonenumber-field[phonenumberslite]
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth','phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    @property
    def phone_formatted(self):
        if self.phone_number == '':
            return ''
        return self.phone_number.as_international
 
    
class Friend(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.lastname
    pass

    
# class GestionFrientPrifile(models.Model):
#     profiles = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
   

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body