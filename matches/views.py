from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import Http404
from django.db.models import Q
from . import forms, models
from datetime import date
from time import time
import os.path
import os

User = get_user_model()
MatchModel = models.MatchModel


def match_is_valid(form):
    global rounds
    cd = form.cleaned_data
    errors = 0
    username = cd.get('p2')
    rounds = []
    score1 = 0
    score2 = 0
    if not User.objects.filter(username=username).exists():
        form.add_error('p2', 'Пользователя не существует')
        return (False, form)

    for i in range(1,6):
        s1 = cd.get(f'set{i}p1')
        s2 = cd.get(f'set{i}p2')
        if s1 == 0 and s2 == 0:
            rounds.append(0)
            continue

        max_score = max((s1, s2))
        min_score = min((s1, s2))
        p1_field = f'set{i}p1'
        p2_field = f'set{i}p2'
        if s1 < 0:
            form.add_error(p1_field, 'Счет не может быть отрицательным')
            errors+=1
        if s2 < 0:
            form.add_error(p2_field, 'Счет не может быть отрицательным')
            errors+=1
        else:
            if s1 == s2:
                form.add_error(p1_field, 'Счет не может быть равен')
                errors+=1
            else:
                if (max_score - min_score) == 1:
                    form.add_error(p1_field, 'Счет должен отличаться, как минимум, на 2 очка')
                    errors+=1
                else:
                    if max_score > 21:
                        if (max_score - min_score) > 2:
                            form.add_error(p1_field, 'Счет после 21 и 11 очков должен отличаться на 2 очка')
                            form.add_error(p2_field, 'Счет после 21 и 11 очков должен отличаться на 2 очка')
                            errors+=1
                    elif (max_score > 11) and (max_score < 21):
                        if (max_score - min_score) != 2:
                            form.add_error(p1_field, 'Счет после 21 и 11 очков должен отличаться на 2 очка')
                            form.add_error(p2_field, 'Счет после 21 и 11 очков должен отличаться на 2 очка')
                            errors+=1
                    else:
                        rounds.append(1)
                        if s1 > s2:
                            score1 += 1
                        else:
                            score2 += 1
    if (score1 + score2) in (4, 6):
        form.add_error(None, 'Сетов может быть 3, 5 или 7')
        errors += 1
    else:
        if ((score1 + score2) == 5 and max(score1, score2) in [4, 5]) or\
            ((score1 + score2) == 7 and max(score1, score2) in [5, 6, 7]):
            form.add_error(None, 'Неверное количество сетов')
            errors += 1
    if errors == 0:
        for i in range(3):
            if rounds[i] != 1:
                errors+=1
                form.add_error(None, 'Первые три раунда обязательны для заполнения')
                break
        for i in range(3, 4):
            prev = rounds[i-1]
            if rounds[i] == 1 and prev == 0:
                errors+=1
                form.add_error(None, f'Пустой раунд {i}')
    else:
        return (False, form)
    if errors == 0:
        rounds = []
        return (True, form, score1, score2)
    else:
        rounds = []
        return (False, form)

def add_user_stat(match):
    private_stat_1 = match.p1.private_stat
    private_stat_2 = match.p2.private_stat
    public_stat_1 = match.p1.public_stat
    public_stat_2 = match.p2.public_stat
    if match.score1 > match.score2:
        private_stat_1.wins += 1
        private_stat_2.loses += 1
        if match.is_public:
            public_stat_1.wins += 1
            public_stat_2.loses+=1
    else:
        private_stat_2.wins += 1
        private_stat_1.loses += 1
        if match.is_public:
            public_stat_2.wins += 1
            public_stat_1.loses+=1

    #добавление сухих побед и поражений
    if match.score1 == 0:
        private_stat_2.dry_wins += 1
        private_stat_1.dry_loses += 1
        if match.is_public:
            public_stat_2.dry_wins += 1
            public_stat_1.dry_loses += 1

    elif match.score2 == 0:
        private_stat_1.dry_wins += 1
        private_stat_2.dry_loses += 1
        if match.is_public:
            public_stat_1.dry_wins += 1
            public_stat_2.dry_loses += 1

    if match.set1p1 > match.set1p2:
        private_stat_1.s1_win += 1
        private_stat_2.s1_l += 1
        if match.is_public:
            public_stat_1.s1_win += 1
            public_stat_2.s1_l += 1
    else:
        private_stat_2.s1_win += 1
        private_stat_1.s1_l += 1
        if match.is_public:
            public_stat_2.s1_win += 1
            public_stat_1.s1_l += 1

    if match.set2p1 > match.set2p2:
        private_stat_1.s2_win += 1
        private_stat_2.s2_l += 1
        if match.is_public:
            public_stat_1.s2_win += 1
            public_stat_2.s2_l += 1
    else:
        private_stat_2.s2_win += 1
        private_stat_1.s2_l += 1
        if match.is_public:
            public_stat_2.s2_win += 1
            public_stat_1.s2_l += 1

    if match.set3p1 > match.set3p2:
        private_stat_1.s3_win += 1
        private_stat_2.s3_l += 1
        if match.is_public:
            public_stat_1.s3_win += 1
            public_stat_2.s3_l += 1
    else:
        private_stat_2.s3_win += 1
        private_stat_1.s3_l += 1
        if match.is_public:
            public_stat_2.s3_win += 1
            public_stat_1.s3_l += 1

    if match.set4p1 != 0 or match.set4p2 != 0:

        if match.set4p1 > match.set4p2:
            private_stat_1.s4_win += 1
            private_stat_2.s4_l += 1
            if match.is_public:
                public_stat_1.s4_win += 1
                public_stat_2.s4_l += 1
        else:
            private_stat_2.s4_win += 1
            private_stat_1.s4_l += 1
            if match.is_public:
                public_stat_2.s4_win += 1
                public_stat_1.s4_l += 1
        if match.set5p1 > match.set5p2:
            private_stat_1.s5_win += 1
            private_stat_2.s5_l += 1
            if match.is_public:
                public_stat_1.s5_win += 1
                public_stat_2.s5_l += 1
        else:
            private_stat_2.s5_win += 1
            private_stat_1.s5_l += 1
            if match.is_public:
                public_stat_2.s5_win += 1
                public_stat_1.s5_l += 1

    private_stat_1.save()
    private_stat_2.save()
    if match.is_public:
        public_stat_1.save()
        public_stat_2.save()

def choice_matches(request):
    return render(request, 'matches/choice.html')

def allMatches(request):
    matches = MatchModel.objects.filter(is_confirmed=True, is_public=True)
    return render(request, 'matches/all_matches.html', {'matches': matches})


class AddMatchView(View):

    def post(self, request):
        form = forms.AddMatchForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get('p2') == request.user:
                form.add_error('p2', 'Вы не можете играть против себя!')
                return render(request, 'matches/create_match.html', {'form': form})
            check = match_is_valid(form)
            result = check[0]
            form = check[1]

            if result:
                p1 = request.user
                p2 = form.cleaned_data.get('p2')
                p2 = User.objects.get(username=p2)
                slug = f'{p1}-{p2}-{str(int(time()))}'
                match = form.save(commit=False)
                match.p1 = p1
                match.score1 = check[2]
                match.score2 = check[3]
                match.slug = slug
                if match.video:
                    match.is_public = True
                match.save()
                return render(request, 'matches/match_added.html')
            else:
                return render(request, 'matches/create_match.html', {'form': form})
        else:
            form.add_error(None, 'Error')
            print(form.errors)
            return render(request, 'matches/create_match.html', {'form': form})

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        form = forms.AddMatchForm
        return render(request, 'matches/create_match.html', {'form': form})



@login_required
def my_matches(request):
    if request.method == 'GET':
        matches = MatchModel.objects.filter(Q(p1=request.user) | Q(p2=request.user))
        not_confirmed = None#matches that not confirmed
        if matches.filter(is_confirmed=False).exists():
            not_confirmed = len(matches.filter(is_confirmed=False))
        matches = matches.filter(is_confirmed=True).order_by('date')
        return render(request, 'matches/my_matches.html', {'matches': matches, 'not_confirmed':not_confirmed})

class DetailMatchView(View):

    def get(self, request, slug):

        if not MatchModel.objects.filter(slug=slug).exists():
            return HttpResponse('404')

        match = MatchModel.objects.get(slug=slug)

        if not match.is_confirmed and request.user == match.p2:
            return HttpResponseRedirect(reverse('confirm_match', kwargs={'slug': slug}))

        if not match.is_public and (request.user not in (match.p1, match.p2)):
            return HttpResponseRedirect(reverse('all_matches'))

        context = {}
        context['match'] = match
        context['video'] = None
        if match.video:
            context['video'] = match.video
        return render(request, 'matches/detail_match.html', context)############!!!!!!!!!


class NotConfirmedView(View):

    def get(self, request):
        matches = MatchModel.objects.filter(p2=request.user, is_confirmed=False)#требует подтверждения самого пользователя
        matches2 = MatchModel.objects.filter(p1=request.user, is_confirmed=False)#матчи которые послал этот пользователь
        return render(request, 'matches/not_confirmed_matches.html', {'matches':matches, 'matches2':matches2})

class ConfirmMatchView(View):

    def get(self, request, slug):
        if MatchModel.objects.filter(slug=slug).exists():
            if not MatchModel.objects.filter(slug=slug, is_confirmed=False):
                raise Http404

            match = MatchModel.objects.get(slug=slug)

            if request.user == match.p1:
                return HttpResponseRedirect(reverse('detail_match', kwargs={'slug':slug}))
            if request.user == match.p2:
                context = {}
                context['match'] = match
                return render(request, 'matches/confirm_match.html', context)
            return HttpResponseRedirect('/')

        raise Http404

    def post(self, request, slug):
        match = MatchModel.objects.get(slug=slug)
        match.is_confirmed = True
        match.save()
        add_user_stat(match)
        return HttpResponse('харош')
