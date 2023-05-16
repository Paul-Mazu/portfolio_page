from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
        )


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    if instance:
        user = instance.user
        user.delete()
