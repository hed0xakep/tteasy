from django.contrib.auth import get_user_model
from . import models, forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def add_post(request):
    if request.method == 'POST':
        form = forms.PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('all_posts'))
        return render(request, 'advt/add_post.html', {'form': form})
    form = forms.PostCreateForm
    return render(request, 'advt/add_post.html', {'form': form})

def all_posts(request):
    if request.method == 'GET':
        posts = models.PostModel.objects.all().order_by('date_pub')
        return render(request, 'advt/all_posts.html', {'posts': posts})
