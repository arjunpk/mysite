from django.forms import ModelForm
from django.contrib.auth.models import User
from Profiles.models import Profiles

class CreateBasicUserForm(ModelForm):
  class Meta:
    model = User
    fields = { 'email', 'first_name', 'last_name' }

class SelectUserTypeForm(ModelForm):
  class Meta:
    model = Profiles
    fields = { 'user_type' }
