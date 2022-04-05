from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate_account/', views.ActivateAccountView.as_view(), name='activate'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', PasswordChangeView.as_view(template_name='account/password_change.html', success_url='/'), name='change_password'),
    path('settings/', views.SettingsPageView.as_view(), name='settings'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
]
