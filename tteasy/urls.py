from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import all_players

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('matches/', include('matches.urls')),
    path('players/', all_players, name='all_players'),
    path('social_auth/', include('social_django.urls')),
    path('advt/', include('advt.urls')),

    path('password_reset/',
        auth_views.PasswordResetView.as_view(template_name='account/reset_password/password_reset.html'),
        name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/reset_password/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/reset_password/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/reset_password/password_reset_complete.html'),
         name='password_reset_complete'),
    path('<user>/', include('stats.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
