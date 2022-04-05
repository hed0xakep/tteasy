from django.urls import path, include
from . import views

urlpatterns = [
    path('<user>/', views.statistics, name='user_statistics')
]
