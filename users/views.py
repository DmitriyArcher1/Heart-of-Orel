from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.cache import cache

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from users.models import User


def login(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)

        if form.is_valid():
            username= request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы успешно вошли в систему")
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'login.html', context)

def registration(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)

        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрировались и  вошли в систему")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'registration.html', context)

@login_required
def profile(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = ProfileForm(data = request.POST, instance = request.user, files = request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлён")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance = request.user)

    context = {
        'title': 'Профиль',
        'form': form,
    }

    return render(request, 'profile.html', context)

def logout(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    # messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)

    return redirect(reverse('main:index'))

# @login_required
# def first_comments(request):
#     form = CommentsForm(instance = request.user)

#     context = {
#         'title': 'Отзывы',
#         'form': form,
#     }

#     return render(request, 'first_comments.html', context)

# class UserRegistrationForm(TemplateView):
#     template_name= 'registration.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['title'] = 'Регистрация'
#         context['content_title'] = ''
#         context['content_text'] = ''

#         return context
    

