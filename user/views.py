from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from .models import PostModel, ResponseModel
from rest_framework import status, generics
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from random import randint
from . import serializers


def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


class CreateProfile(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
