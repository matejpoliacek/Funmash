from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



# Create your models here.

class Image(models.Model):

    # name of image in filesysem, serves as unique ID
    name = models.IntegerField(primary_key=True, default="placeholder_name")

    # filepath in filesystem
    source = models.CharField(max_length=255, default="")

    # ranking of the file (higher = better)
    ranking = models.PositiveIntegerField(default=0)
	
    # Username of user who uploaded the picture
    owner = models.CharField(max_length=255, default = "Nobilitie")

    # FUTURE VERSION SUGGESTED ATTRIBUTES:
    # battles (set of other image names with which it competed - these must not be shown again with this image)
    # category (tags to classify images, e.g. cats, memes, dry, stereotype, fail, ...
    # expected ranking (for when advanced ranking algorithm is in place)
    # losses
    # wins - both of these aren't really needed..?

    def __str__(self):
        return str(self.name)
		
		
class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    # Additional attributes we might want to include.
    # website = models.URLField(blank=True)
    # list / dictionary of uploaded images (image name in media or its ID in media)
    # profile image

    def __unicode__(self):
        return self.user.username
		




