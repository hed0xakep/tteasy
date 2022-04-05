from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.players_list, name='players_list')
]
