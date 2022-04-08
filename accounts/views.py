from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.views.generic import View
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CustomUser
from random import randint
from . import forms


def generate_code():
    code = ''
    for i in range(4):
        code+=str(randint(0, 9))
    return code

class RegisterView(View):
    def post(self, request):
        form = forms.CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            if CustomUser.objects.filter(email=email).exists():
                form.add_error('email', 'User with this email already exists')
                return render(request, 'account/register.html', {'form': form})

            else:
                form.save()
                print(request.FILES)
                user =  CustomUser.objects.get(email=email)
                user.is_active = False
                user.save()
                code = generate_code()
                print('------------CODE------------\n',code,'\n------------CODE------------')
                request.session['username'] = username
                request.session['code'] = code
                send_mail('tteasy', code, settings.EMAIL_HOST_USER, (email,))
                return HttpResponseRedirect('/account/activate_account')

        return render(request, 'account/register.html', {'form': form})

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form = forms.CustomUserCreationForm
        return render(request, 'account/register.html', {'form': form})



class ActivateAccountView(View):

    def post(self, request):
        form = forms.Enter_code(request.POST)
        if form.is_valid():
            if request.session['code'] == form.cleaned_data.get('code'):
                username = request.session['username']
                user = CustomUser.objects.get(username=username)
                user.is_active = True
                pub_stat = PublicStatisticsModel.objects.create()
                private_stat = PrivateStatisticsModel.objects.create()
                user.private_stat = private_stat
                user.public_stat = pub_stat
                user.save()
                return HttpResponseRedirect('/account/login/')

            form.add_error(None, 'Неверный код')
            return render(request, 'account/confirmation_code.html', {'form': form})

        return render(request, 'account/confirmation_code.html', {'form': form})

    def get(self, request):
        if request.user.is_active:
            return HttpResponseRedirect('/')
        form = forms.Enter_code
        return render(request, 'account/confirmation_code.html', {'form': form})

def custom_login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    match request.method:
        case 'POST':
            form = forms.LoginForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        request.session['username'] = username
                        email = user.email
                        code = generate_code()
                        print('------------CODE------------\n',code,'\n------------CODE------------')
                        request.session['code'] = code
                        send_mail('tteasy', code, settings.EMAIL_HOST_USER, (email,)) вернуть в релиз
                        return HttpResponseRedirect('/account/activate_account')
                else:
                    form.add_error(None, 'Неправильный логин или пароль')
                    return render(request, 'account/login.html', {'form': form})

            return render(request, 'account/login.html', {'form': form})

        case 'GET':
            form = forms.LoginForm
            return render(request, 'account/login.html', {'form': form})



class SettingsPageView(View):

    def post(self, request):
        form = forms.CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'account/profile_settings.html', {'form':form})
        return render(request, 'account/profile_settings.html', {'form':form})

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        user = CustomUser.objects.get(username=request.user.username)
        print(user, 'sdfsdfs',)
        form = forms.CustomUserChangeForm(instance=user)
        return render(request, 'account/profile_settings.html', {'form':form})


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            #default_token_generator = PasswordResetTokenGenerator()
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)  # email в форме регистрации проверен на уникальность
            subject = 'Запрошен сброс пароля'
            cont = {
                "email": user.email,
                'domain': settings.DOMAIN,  # доменное имя сайта
                'site_name': 'Website',  # название своего сайта
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),  # шифруем идентификатор
                "user": user,  # чтобы обратиться в письме по логину пользователя
                'token': default_token_generator.make_token(user),  # генерируем токен
                'protocol': 'http',
            }
            msg_html = render_to_string('account/reset_password/recover_password_mail.html', cont)
            send_mail(subject, 'ссылка', 'admin@django-project.site', [user.email], fail_silently=True,
                          html_message=msg_html)
            return redirect('password_reset_done')
        return render(request, template_name="account/reset_password/password_reset.html",
            context={"password_reset_form": form})

    form = PasswordResetForm()
    return render(request, template_name="account/reset_password/password_reset.html",
                context={"password_reset_form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
