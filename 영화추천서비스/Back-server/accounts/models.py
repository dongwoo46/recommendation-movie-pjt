from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    sex = models.TextField()
    username = models.CharField(max_length=100, unique=True)
    introduction = models.TextField()
    height = models.CharField(max_length=100)
    body_shape = models.CharField(max_length=100)
    ideal_type = models.TextField(blank = True)
    face = models.CharField(max_length=100, blank = True)
    profile_img1 = models.ImageField(blank = True)
    profile_img2 = models.ImageField(blank = True)
    profile_img3 = models.ImageField(blank = True)
    profile_img4 = models.ImageField(blank = True)
    living = models.CharField(max_length=50, blank = True)
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
