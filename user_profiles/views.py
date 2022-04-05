from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import Http404
from matches.models import MatchModel
from django.db.models import Q

# Create your views here.
CustomUser = get_user_model()

def showprofile(request, user):

    if not CustomUser.objects.filter(username=user).exists():
        raise Http404
    user = CustomUser.objects.get(username=user)
    matches = MatchModel.objects.filter(Q(p1=user) | Q(p2=user), is_confirmed=True)
    context = {}
    context['user'] = user
    context['matches'] = matches
    if user.gender == 'm':
        context['gender'] = 'Мужской'
    else:
        context['gender'] = 'Женский'
    return render(request, 'profiles/profile.html', context)
