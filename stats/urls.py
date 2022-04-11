from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showprofile, name='profile'),
    path('stats/', views.statistics, name='user_statistics')
]
