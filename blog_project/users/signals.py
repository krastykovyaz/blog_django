from django.db.models.signals import post_save # signal when the user was created
from django.contrib.auth.models import User #sender the signal
from django.dispatch import receiver # check signal
from .models import Profile

@receiver(post_save, sender=User) # when the user is sent then send the signal post_save ang the signal going by receiver which create_profile function
def create_profile(sender, instance, created, **kwargs): # **kwargs means except any additional arguments
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
