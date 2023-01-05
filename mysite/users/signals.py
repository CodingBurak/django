from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.forms import RegisterForm

from .models import Profile

@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance, location="Germany")
    
# can be done in single call as well
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()
    

