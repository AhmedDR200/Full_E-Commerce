from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50, default='', blank=True)
    reset_password_expire = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    
    if created:
        profile = Profile(user=user)
        profile.save()

        
    