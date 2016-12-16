from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpRedirect

def index(request):
  return HttpRedirect("/")
  #Placeholder - Redirect to homepage here
