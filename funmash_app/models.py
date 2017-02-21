from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Image(models.Model):
    # id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=128)
    # location_bdg = models.CharField(max_length=128)
    # location_detail = models.CharField(max_length=255)
    # upvotes = models.IntegerField(default=0)
    # images = models.ImageField(upload_to='issue_images')

    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.id


class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    # Additional attributes we might want to include.
    # website = models.URLField(blank=True)
    # list / dictionary of uploaded images (image name in media or its ID in media)

    image = models.ImageField(upload_to='', blank=True)

    def __unicode__(self):
        return self.user.username