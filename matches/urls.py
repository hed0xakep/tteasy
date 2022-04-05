from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.choice_matches, name='matches'),###########
    path('add/', views.AddMatchView.as_view(), name='add_match'),
    path('all/', views.allMatches, name='all_matches'),
    path('my/', views.my_matches, name = 'my_matches'),#########
    path('match/<slug>', views.DetailMatchView.as_view(), name='detail_match'),
    path('not_confirmed/', views.NotConfirmedView.as_view(), name='not_confirmed'),
    path('confirm/<slug>', views.ConfirmMatchView.as_view(), name='confirm_match')
]
