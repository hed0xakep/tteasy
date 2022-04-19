from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import ( HttpResponse,
                        HttpResponseNotFound,
                        HttpResponseRedirect,
                        Http404 )
from django.shortcuts import render
from matches.models import MatchModel
from stats.models import PublicStatisticsModel
from django.db.models import Q


User = get_user_model()

def percents(val, val2):#функция принимает два числа и возвращает их пропорцию в процентах
    percent = (val+val2)/100
    if percent == 0:
        return (0, 0)
    percents1 = round(val/percent, 1)
    percents2 = round(val2/percent, 1)
    return (percents1, percents2)

def get_user_place(user, criterion):
    stats_models = list(PublicStatisticsModel.objects.all().order_by(criterion))
    place = 1
    for model in stats_models:
        print(model.user)
        print(model.wins)
        if model.user == user:
            return place
        else:
            place +=1

def showprofile(request, user):
    if not User.objects.filter(username=user).exists():
        raise Http404
    user = User.objects.get(username=user)
    matches = MatchModel.objects.filter(Q(p1=user) | Q(p2=user), is_confirmed=True)
    win_place = get_user_place(user, 'wins')
    print(win_place, 'place')
    context = {}
    context['user'] = user
    context['matches'] = matches
    if user.gender == 'm':
        context['gender'] = 'Мужской'
    else:
        context['gender'] = 'Женский'
    return render(request, 'profiles/profile.html', context)

def statistics(request, user):
    ###################################################################
    #переменные с припиской private относятся к приватной статистике,#
    #все остальное - к публичной                                      #
    ###################################################################
    if not User.objects.filter(username=user).exists():
        raise Http404
    context = {}

    user = User.objects.get(username=user)
    private_stat = user.private_stat#приватная стата игрока и публичная
    public_stat = user.public_stat

    games = public_stat.wins + public_stat.loses
    wins = public_stat.wins
    loses = public_stat.loses
    dry_wins = public_stat.dry_wins
    dry_loses = public_stat.dry_loses
    wins_perc, loses_perc = percents(public_stat.wins, public_stat.loses)#процент побед/поражений

    win_sets = public_stat.s1_win + public_stat.s2_win + public_stat.s3_win + public_stat.s4_win + public_stat.s5_win#колчичество выигранных/проигранных сетов
    lose_sets = public_stat.s1_l + public_stat.s2_l + public_stat.s3_l + public_stat.s4_l + public_stat.s5_l

    win_s1_perc, lose_s1_perc = percents(public_stat.s1_win, public_stat.s1_l)#проценты выигрыша/проигрыша в сетах
    win_s2_perc, lose_s2_perc = percents(public_stat.s2_win, public_stat.s2_l)
    win_s3_perc, lose_s3_perc = percents(public_stat.s3_win, public_stat.s3_l)
    win_s4_perc, lose_s4_perc = percents(public_stat.s4_win, public_stat.s4_l)
    win_s5_perc, lose_s5_perc = percents(public_stat.s5_win, public_stat.s5_l)

    context['user'] = user
    context['games'] = games
    context['wins'] = wins
    context['loses'] = loses
    context['dry_wins'] = dry_wins
    context['dry_loses'] = dry_loses
    context['wins_perc'] = wins_perc
    context['loses_perc'] = loses_perc
    context['win_sets'] = win_sets
    context['lose_sets'] = lose_sets
    context['win_s1_perc'] = win_s1_perc
    context['win_s2_perc'] = win_s2_perc
    context['win_s3_perc'] = win_s3_perc
    context['win_s4_perc'] = win_s4_perc
    context['win_s5_perc'] = win_s5_perc
    context['lose_s1_perc'] = lose_s1_perc
    context['lose_s2_perc'] = lose_s2_perc
    context['lose_s3_perc'] = lose_s3_perc
    context['lose_s4_perc'] = lose_s4_perc
    context['lose_s5_perc'] = lose_s5_perc

    if not user == request.user:
        return render(request, 'stats/user_statistics.html', context)
    '''
    Все то же самое что сверху, только данные взяты из приватной статистики
    '''

    games_private = private_stat.wins + private_stat.loses
    wins_private = private_stat.wins
    loses_private = private_stat.loses
    dry_wins_private = private_stat.dry_wins
    dry_loses_private = private_stat.dry_loses
    wins_perc_private, loses_perc_private = percents(private_stat.wins, private_stat.loses)

    win_sets_private = private_stat.s1_win + private_stat.s2_win + private_stat.s3_win + private_stat.s4_win + private_stat.s5_win
    lose_sets_private = private_stat.s1_l + private_stat.s2_l + private_stat.s3_l + private_stat.s4_l + private_stat.s5_l

    win_s1_perc_private, lose_s1_perc_private = percents(private_stat.s1_win, private_stat.s1_l)
    win_s2_perc_private, lose_s2_perc_private = percents(private_stat.s2_win, private_stat.s2_l)
    win_s3_perc_private, lose_s3_perc_private = percents(private_stat.s3_win, private_stat.s3_l)
    win_s4_perc_private, lose_s4_perc_private = percents(private_stat.s4_win, private_stat.s4_l)
    win_s5_perc_private, lose_s5_perc_private = percents(private_stat.s5_win, private_stat.s5_l)

    context['games_private'] = games_private
    context['wins_private'] = wins_private
    context['loses_private'] = loses_private
    context['dry_wins_private'] = dry_wins_private
    context['dry_loses_private'] = dry_loses_private
    context['wins_perc_private'] = wins_perc_private
    context['loses_perc_private'] = loses_perc_private
    context['win_sets_private'] = win_sets_private
    context['lose_sets_private'] = lose_sets_private
    context['win_s1_perc_private'] = win_s1_perc_private
    context['win_s2_perc_private'] = win_s2_perc_private
    context['win_s3_perc_private'] = win_s3_perc_private
    context['win_s4_perc_private'] = win_s4_perc_private
    context['win_s5_perc_private'] = win_s5_perc_private
    context['lose_s1_perc_private'] = lose_s1_perc_private
    context['lose_s2_perc_private'] = lose_s2_perc_private
    context['lose_s3_perc_private'] = lose_s3_perc_private
    context['lose_s4_perc_private'] = lose_s4_perc_private
    context['lose_s5_perc_private'] = lose_s5_perc_private

    return render(request, 'stats/my_statistics.html', context)
