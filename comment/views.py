import re
from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.cache import cache

from comment.forms import CommentForm, SecondCommentForm, ThirdCommentForm, FourthCommentForm
from comment.models import Comment, SecondComment, ThirdComment, FourthComment
from users.views import login

@login_required
def first_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = Comment.objects.all() # получение всех комментариев из первой таблицы
    if request.method == 'POST':
        form = CommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = Comment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:first_comments'))
        else:
            return render(request, 'comment/first_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})
    
    else:
        form = CommentForm()
        return render(request, 'comment/first_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})

@login_required
def second_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = SecondComment.objects.all() # Получение всех записей комментариев из второй таблицы
    if request.method == 'POST':
        form = SecondCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = SecondComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:second_comments'))
        else:
            return render(request, 'comment/second_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})
    
    else:
        form = SecondCommentForm()
        return render(request, 'comment/second_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})

@login_required
def third_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = ThirdComment.objects.all()
    if request.method == 'POST':
        form = ThirdCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = ThirdComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:third_comments'))
        else:
            return render(request, 'comment/third_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})
    
    else:
        form = ThirdCommentForm()
        return render(request, 'comment/third_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})
    
@login_required
def fourth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = FourthComment.objects.all()
    if request.method == 'POST':
        form = FourthCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = FourthComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:fourth_comments'))
        else:
            return render(request, 'comment/fourth_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})
    
    else:
        form = FourthCommentForm()
        return render(request, 'comment/fourth_comments.html', {'form': form, 'comments': comments, 'title': 'Отзывы', 'user': request.user})


@login_required
def delete_first_comment(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(Comment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:first_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_second_comment(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(SecondComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:second_comments'))
    else:
        raise PermissionError

@login_required
def delete_third_comment(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(ThirdComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:third_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_fourth_comments(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(FourthComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:fourth_comments'))
    else:
        raise PermissionError
