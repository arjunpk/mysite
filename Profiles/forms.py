from django.forms import ModelForm
from django.contrib.auth.models import User
from Profiles.models import Profiles

class CreateBasicUserForm(ModelForm):
  class Meta:
    model = User
    fields = { 'email', 'first_name', 'last_name' }
    """
    def verify_email(self):
		  email = self.cleaned_data.get('email')
		  if email and User.objects.filter(email=email).count():
        raise forms.ValidationError(u'There is already an account with this email id.')
    """

class SelectUserTypeForm(ModelForm):
  class Meta:
    model = Profiles
    fields = { 'user_type' }
