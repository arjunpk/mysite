from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^$', views.index, name='index'),
  #Placeholder - need to fix with usernames
  url(r'^album/', include('Media/urls)), 
]
