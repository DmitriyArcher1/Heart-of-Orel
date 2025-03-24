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

from comment.forms import CommentForm
from comment.models import Comment

@login_required
def first_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == 'POST':
        form = CommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = Comment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:comments'))
        else:
            return render(request, 'comment/first_comments.html', {'form': form, 'title': 'Отзывы'})
    
    else:
        form = CommentForm()
        return render(request, 'comment/first_comments.html', {'form': form, 'title': 'Отзывы'})