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
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  
class Media(models.Model):
  user = models.ForeignKey(User)
  album = models.ForeignKey(Albums)
  MEDIA_TYPE_CHOICES = (
    (1, 'Photo'),
    (2, 'Video'),
  )
  media_type=models.PositiveSmallIntegerField('Media Type',
                                              choices=MEDIA_TYPE_CHOICES,
                                              blank=False,
                                              null=False)
  title = models.CharField(max_length=50, blank=True)
  desc = models.CharField(max_length=150, blank=True)
  orig_extension = models.CharField(max_length=5, blank=False)
  #If image is imported from social network, we do not need to store the original image or resize them.
  #Unless we allow import from 500px if possible and if 500px gives larger file formats
  #Need to change to File Field
  original_media_file = models.CharField(max_length=100, blank=True)
  display_media_file = models.CharField(max_length=100, blank=False)
  thumb_media_file = models.CharField(max_length=100, blank=False)
  share_to_fb = models.BooleanField()
  share_to_tw = models.BooleanField()
  share_to_ig = models.BooleanField()
  up_votes = models.IntegerField()
  down_votes = models.IntegerField()
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

class Media_alt_Res(models.Model):
  """This class holds media in alternative resolutions. The main class stores the default resolution for the website.
  In this class, media details of varying resolutions are stored in order to provide the capability of upgrades"""
  media = models.ForeignKey(Media)
  RES_CHOICES = (
    (1, '480p'),
    (2, '720p'),
    (3, '1080p'),
  )
  resolution = models.PositiveSmallIntegerField('Resolution',
                                                choices=RES_CHOICES,
                                                blank=False,
                                                null=False)
  media_file = models.CharField(max_length=100, blank=False)
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
class Media_Reports(models.Model):
  """Placeholder. Needs to be modified. This class holds the reports on the media by users for violation of Terms of Use"""
  media = models.ForeignKey(Media)
  report = models.CharField(max_length=1000)
  reported_by=models.ForeignKey(User, related_name='Reported_By')
  action_taken = models.BooleanField()
  action_desc = models.CharField(max_length=1000)
  action_taken_by=models.ForeignKey(User, related_name='Action_Taken_By')
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  



