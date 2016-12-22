from django.conf.urls import url, include
from . import views

urlpatterns=[
  #/profile
  url(r'^$', views.index, name='index'),
  #/profile/<uid/username>
  url(r'^(?P<user_name_id>[A-Za-z0-9_]+)$', views.detail, name='user_profile'),
  #/profile/<uid/username>/album
  url(r'^(?P<user_name_id>[A-Za-z0-9_]+)/album/', include('media.urls')),
  #/profile/reset_password
  url(r'^reset_password/$', views.change_password, name='change_password'),
]
