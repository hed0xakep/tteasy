from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('add_post/', views.add_post, name='add_post')
]
