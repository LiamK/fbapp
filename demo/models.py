from django.db import models
from django.contrib.auth.models import User
from django_facebook.models import FacebookProfileModel

class UserProfile(FacebookProfileModel):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.user.__unicode__()
