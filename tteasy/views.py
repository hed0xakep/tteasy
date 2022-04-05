from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()

def all_players(request):
    players = UserModel.objects.filter(is_active=True)
    return render(request, 'profiles/all_players.html', {'players':players})
