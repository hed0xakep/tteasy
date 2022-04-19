from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/create/', views.CreateProfile.as_view(), name='profile')
]
