from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Homepost
from . import forms

# Create your views here.

def show_homepage(request):
	homepost = Homepost.objects.all()
	return render(request, 'homepage/index.html', {
		'posts': homepost
	})

def post_detail(request, slug):
	post = Homepost.objects.get(slug__iexact=slug)
	return render(request, 'homepage/post_detail.html', context={
	'post1': post
	})


class CreatePostView(View):

	def get(self, request):
		if not request.user.is_staff:
			return HttpResponseRedirect('/')
		form = forms.CreatePostForm()
		return render(request, 'homepage/create_post.html', context={'form': form})

	def post(self, request):
		if not request.user.is_staff:
			return HttpResponseRedirect('/')

		bound_form = forms.CreatePostForm(request.POST)

		if bound_form.is_valid():
			new_post = bound_form.save()
			return redirect(new_post)
			
		return render(request, 'homepage/create_post.html', context={'form': bound_form})
