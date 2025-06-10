import re
from urllib import request
from webbrowser import get
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
from pkg_resources import get_distribution

from comment.forms import *
from comment.models import *
from users.views import login


# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Функции для добавления комментариев
@login_required
def first_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = Comment.objects.all() # получение всех комментариев из первой таблицы
    if request.method == 'POST':
        form = CommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = Comment(text = text, author = request.user)
            comment.save()
            # messages.success(request, "Комментарий добавлен")

            return redirect(reverse('comment:first_comments'))
        else:
            return render(request, 'comment/first_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = CommentForm()
        return render(request, 'comment/first_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})

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
            return render(request, 'comment/second_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = SecondCommentForm()
        return render(request, 'comment/second_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})

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
            return render(request, 'comment/third_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = ThirdCommentForm()
        return render(request, 'comment/third_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
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
            return render(request, 'comment/fourth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = FourthCommentForm()
        return render(request, 'comment/fourth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
@login_required
def fifth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = FifthComment.objects.all()
    if request.method == 'POST':
        form = FifthCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = FifthComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:fifth_comments'))
        else:
            return render(request, 'comment/fifth_comment.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = FifthCommentForm()
        return render(request, 'comment/fifth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
@login_required
def sixth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = SixthComment.objects.all()
    if request.method == 'POST':
        form = SixthCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = SixthComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:sixth_comments'))
        else:
            return render(request, 'comment/sixth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = SixthCommentForm()
        return render(request, 'comment/sixth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
@login_required
def seventh_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = SeventhComment.objects.all()
    if request.method == 'POST':
        form = SeventhCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = SeventhComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:seventh_comments'))
        else:
            return render(request, 'comment/seventh_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = SeventhCommentForm()
        return render(request, 'comment/seventh_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})

@login_required
def eigth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = EigthComment.objects.all()
    if request.method == 'POST':
        form = EigthCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = EigthComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:eigth_comments'))
        else:
            return render(request, 'comment/eigth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    else:
        form = EigthCommentForm()
        return render(request, 'comment/eigth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
@login_required
def nineth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = NinethComment.objects.all()
    if request.method == 'POST':
        form = NinethCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = NinethComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:nineth_comments'))
        else:
            return render(request, 'comment/nineth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    else:
        form = NinethCommentForm()
        return render(request, 'comment/nineth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
@login_required
def tenth_comments(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    comments = TenthComment.objects.all()
    if request.method == 'POST':
        form = TenthCommentForm(data = request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            comment = TenthComment(text = text, author = request.user)
            comment.save()

            return redirect(reverse('comment:tenth_comments'))
        else:
            return render(request, 'comment/tenth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
    
    else:
        form = TenthCommentForm()
        return render(request, 'comment/tenth_comments.html', {'form': form, 'comments': comments, 'title': 'Комментарии', 'user': request.user})
# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Функции удаления комментариев
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

@login_required
def delete_fifth_comments(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(FifthComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:fifth_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_sixth_comments(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(SixthComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:sixth_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_seventh_comments(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(SeventhComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:seventh_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_eigth_comments(request, comment_id) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(EigthComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:eigth_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_nineth_comments(request, comment_id: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(NinethComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:nineth_comments'))
    else:
        raise PermissionError
    
@login_required
def delete_tenth_comments(request, comment_id: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    comment = get_object_or_404(TenthComment, id = comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        return redirect(reverse('comment:tenth_comments'))
    else:
        raise PermissionError
# -------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------