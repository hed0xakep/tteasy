from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.conf import settings
from . import serializers
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
'''
def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
'''

class CreateProfile(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
