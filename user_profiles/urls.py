from django.urls import path, include
from django.http import HttpResponse, HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.showprofile, name='profile')
]
