from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'xotographers/index.html')