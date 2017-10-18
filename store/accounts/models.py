from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	"""Define which packages user has installed"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	packages_installs = JSONField(blank=True)

#~ @receiver(post_save, sender=User)
#~ def create_user_profile(sender, instance, created, **kwargs):
    #~ if created:
        #~ Profile.objects.create(user=instance)

#~ @receiver(post_save, sender=User)
#~ def save_user_profile(sender, instance, **kwargs):
    #~ instance.profile.save()
