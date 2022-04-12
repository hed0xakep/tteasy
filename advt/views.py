from django.contrib.auth import get_user_model
from . import models, forms
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime as dt

'''
my_string = "07.02.3000"
my_dt = dt.datetime.strptime(my_string, '%d.%m.%Y')'''

@login_required
def add_post(request):
    if request.method == 'POST':
        form = forms.PostCreateForm(request.POST)
        if form.is_valid():
            now = dt.datetime.now()
            del_date = form.cleaned_data['del_date']
            if dt.datetime.strptime(del_date, '%d.%m.%Y') < now:
                response = {
                    'success': False,
                    'message': 'Неверная дата'
                }
                return JsonResponse(response)

            post = form.save(commit=False)
            post.user = request.user
            post.del_date = dt.datetime.strptime(del_date, '%d.%m.%Y')
            post.save()
            response = {
                'sucess': True,
                'message': 'Successfully created'
                    }
            return JsonResponse(reponse)
        response = {
                'errors': form.errors
        }
        return JsonResponse(response)
    form = forms.PostCreateForm
    now = dt.datetime.now()
    return render(request, 'advt/add_post.html', {'form': form, 'now': now})

def all_posts(request):
    if request.method == 'GET':
        posts = models.PostModel.objects.all().order_by('date_pub')
        return render(request, 'advt/all_posts.html', {'posts': posts})
