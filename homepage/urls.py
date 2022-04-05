from django.urls import path, include
from django.http import HttpResponse
from . import views




urlpatterns = [
    path('', views.show_homepage, name ='home_show'),
    path('post/create/', views.CreatePostView.as_view(), name='create_post_url'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
]
