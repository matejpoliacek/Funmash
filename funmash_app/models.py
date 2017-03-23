from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Image(models.Model):

    # name of image in filesysem, serves as unique ID
    name = models.IntegerField(primary_key=True, default="placeholder_name")

    # filepath in filesystem
    source = models.CharField(max_length=255, default="")

    # ranking of the file (higher = better)
    ranking = models.PositiveIntegerField(default=0)
	
    # Username of user who uploaded the picture
    owner = models.CharField(max_length=255, default = "Nobilitie")

    def __str__(self):
        return str(self.name)
		
		
class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
		




