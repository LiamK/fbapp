from django.db import models
from django.contrib.auth.models import User
from django_facebook.models import FacebookProfileModel
from django.db.models.signals import post_save

class UserProfile(FacebookProfileModel):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.user.__unicode__()

# Make sure we create a MyCustomProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)
