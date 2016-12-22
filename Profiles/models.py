from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Categories(models.Model):
	category_name = models.CharField(max_length=50, blank=False)
	USER_TYPE_CHOICES = (
		(1, 'Photographer'),
		(2, 'Service Provider'),
	)
	user_type = models.PositiveSmallIntegerField('user type',
						     choices=USER_TYPE_CHOICES,
						     blank=False,
						     null=False)
	
class Countries(models.Model):
	country_code = models.CharField(max_length=2, blank=False)
	country_name = models.CharField(max_length=50, blank=False)
	
class States(models.Model):
	country = models.ForeignKey(Countries)
	state_name = models.CharField(max_length=50, blank=False)
	
class Cities(models.Model):
	country = models.ForeignKey(Countries)
	state = models.ForeignKey(States)
	city_name = models.CharField(max_length=50, blank=False)
	
class ZipCodes(models.Model):
	country = models.ForeignKey(Countries)
	state = models.ForeignKey(States)
	city = models.ForeignKey(Cities)
	zip_code = models.CharField(max_length=50, blank=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	uid = models.CharField(max_length=20, unique=True, default=None)
	bio = models.CharField(max_length=500, blank=True)
	tag_line = models.CharField(max_length=100, blank=True)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	birth_date = models.DateField(null=True, blank=True)
	GENDER_CHOICES = (
		(1, 'Male'),
		(2, 'Female'),
	)
	gender = models.PositiveSmallIntegerField('gender',
						  choices=GENDER_CHOICES,
						  blank=True,
						  null=True)
	USER_TYPE_CHOICES = (
		(1, 'Photographer'),
		(2, 'Service Provider'),
		(3, 'Customer'),
		(4, 'Explore Mode'),
	)
	user_type = models.PositiveSmallIntegerField('user type',
						     choices=USER_TYPE_CHOICES,
						     blank=False,
						     null=False,
						     default=4)
	start_price_range = models.IntegerField(blank=True, null=True)
	end_price_range = models.IntegerField(blank=True, null=True)
	profile_views = models.IntegerField(blank=False, default=0)
	fb_profile_connected = models.BooleanField(default=False, blank=False, null=False)
	fb_profile = models.CharField(max_length=500, blank=True)
	fb_page_connected = models.BooleanField(default=False, blank=False, null=False)
	fb_page = models.CharField(max_length=500, blank=True)
	tw_profile_connected = models.BooleanField(default=False, blank=False, null=False)
	tw_profile = models.CharField(max_length=500, blank=True)
	ig_profile_connected = models.BooleanField(default=False, blank=False, null=False)
	ig_profile = models.CharField(max_length=500, blank=True)
	email_confirmed = models.BooleanField(default=False, blank=False, null=False)
	follows = models.ManyToManyField(User, related_name='followed_by')
	blocked = models.ManyToManyField(User, related_name='blocked_by')
	
	
	
"""	
In [1]: tim, c = User.objects.get_or_create(username='tim')

In [2]: chris, c = User.objects.get_or_create(username='chris')

In [3]: tim.userprofile.follows.add(chris.userprofile) # chris follows tim

In [4]: tim.userprofile.follows.all() # list of userprofiles of users that tim follows
Out[4]: [<UserProfile: chris>]

In [5]: chris.userprofile.followed_by.all() # list of userprofiles of users that follow chris
Out[5]: [<UserProfile: tim>]

"""
	def __unicode__(self):
		return [self.user.id, self.uid]
	
	def get_absolute_url(self):
		return reverse('profile:detail', kwargs={'pk': self.uid})
	
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
			

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		if instance.profile.uid is None:
			instance.profile.uid=uuid.uuid1().int>>64
		instance.profile.save()
"""
@property 
def percentage_complete(self):
    percent = { 'name': 10, 'mobile': 50, 'website': 10, 'location': 10, 'birth_date': 10, 'gender': 10}
    total = 0
    if self.gender:
        total += percent.get('gender', 0)
    if self.name:
        total += percent.get('name', 0)
    #and so on
    return "%s"%(total)	
"""
	


