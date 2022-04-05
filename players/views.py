from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
CustomUser = get_user_model()

def players_list(request):
    players = CustomUser.objects.filter(is_active=True)
    return render(request, 'players/players_list.html', {'players': players})
