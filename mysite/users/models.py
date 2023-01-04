from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.ImageField(default="default_pic.png",upload_to="profile_pictures")
  description = models.CharField(max_length=50, default="new profile desc")
  location = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.user.username