from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Albums(models.Model):
  user = models.ForeignKey(User)
  album_name = models.CharField(max_length=50, blank=False)
  album_desc = models.CharField(max_length=150, blank=True)
  share_to_fb = models.BooleanField()
  has_photos = models.BooleanField()
  total_media = models.IntegerField()
  create_date = models.DateTimeField()
  
  
class Photos(models.Model):
  user = models.ForeignKey(User)
  album = models.ForeignKey(Album)
  photo_title = models.CharField(max_length=50, blank=True)
  photo_desc = models.CharField(max_length=150, blank=True)
  original_image = models.CharField(max_length=100, blank=True)
  display_image = models.CharField(max_length=100, blank=False)
  thumb_image = models.CharField(max_length=100, blank=False)
  share_to_fb = models.BooleanField()
  share_to_tw = models.BooleanField()
  share_to_ig = models.BooleanField()
  up_votes = models.IntegerField()
  down_votes = models.IntegerField()

class Videos(models.Model):
  user = models.ForeignKey(User)
  album = models.ForeignKey(Album)
  video_title = models.CharField(max_length=50, blank=True)
  video_desc = models.CharField(max_length=150, blank=True)
  original_video = models.CharField(max_length=100, blank=True)
  display_video = models.CharField(max_length=100, blank=False)
  thumb_video = models.CharField(max_length=100, blank=False)
  share_to_fb = models.BooleanField()
  share_to_tw = models.BooleanField()
  share_to_ig = models.BooleanField()


