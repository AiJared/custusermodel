from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from numpy import right_shift


class customManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_admin=False, is_active=True, is_staff=False, is_student=False, is_teacher=False):
        if not email:
            raise ValueError("Users must have an email!")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have a username")

        user_obj = self.model(
            email = self.normalize_email(email), username=username
        )
        
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.is_teacher = is_teacher
        user_obj.is_student = is_student
        user_obj.save(using=self._db)
        return user_obj

class User(AbstractBaseUser):
    username = models.CharField(max_length=63, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = customManager()