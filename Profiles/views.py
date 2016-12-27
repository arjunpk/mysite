from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import Categories, Countries, States, Cities, ZipCodes, Profiles
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse, Http404
from .forms import CreateBasicUserForm, SelectUserTypeForm


def index(request):
  return Http404
  
def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)  # Important!
      messages.success(request, 'Your password was successfully updated!')
      return redirect('profiles:change_password')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'profiles/change_password.html', {
    'form': form
  })
"""
# @login_required
# @transaction.atomic """
def update_profile(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, _('Your profile was successfully updated!'))
      return redirect('settings:profile')
    else:
      messages.error(request, _('Please correct the error below.'))
  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return render(request, 'profiles/profile.html', {
    'user_form': user_form,
    'profile_form': profile_form
  })

"""
# @transaction.atomic"""
def detail(request, user_name_id):
    try:
        user = User.objects.filter(username=user_name_id).select_related('Profiles')
    except User.DoesNotExist:
        try:
            user = User.objects.all().select_related('Profiles').filter(uid=user_name_id)
        except User.DoesNotExist:
            raise Http404
    return render( request,'profiles/user_profile.html', {"user" : user} )

