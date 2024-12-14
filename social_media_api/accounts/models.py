from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self', 
        related_name='followers',  # This will give you reverse access from the other side
        symmetrical=False,  # Users can follow other users without mutual following
        blank=True
    )
    def __str__(self):
        return self.username
    
