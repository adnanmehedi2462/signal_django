from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


@receiver (post_save,sender=User)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
     
@receiver (post_save,sender=User)
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()



__init__.py####################################
from email.policy import default


default_app_config='USER.apps.UserConfig'


App.py#################################################
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'USER'
    def ready(self):
        import USER.signals
        
