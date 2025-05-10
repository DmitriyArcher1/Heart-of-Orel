from django import forms

from comment.models import *

class CommentForm(forms.Form):

    class Meta:
        model = Comment
        fields = (
            'text',
            'author',
        )
    
    text = forms.CharField()
    author = forms.CharField()

class SecondCommentForm(forms.Form):

    class Meta:
        model = SecondComment
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class ThirdCommentForm(forms.Form):

    class Meta:
        model = ThirdComment
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class FourthCommentForm(forms.Form):

    class Meta:
        model = FourthComment
        fields = (
           'text',
           'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class FifthCommentForm(forms.Form):

    class Meta:
        model = FifthComment()
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class SixthCommentForm(forms.Form):

    class Meta:
        model = SixthComment()
        fields = (
            'text',
            'author',
        )
    
    text = forms.CharField()
    author = forms.CharField()

class SeventhCommentForm(forms.Form):

    class Meta:
        model = SeventhComment()
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class EigthCommentForm(forms.Form):

    class Meta:
        model = EigthComment()
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class NinethCommentForm(forms.Form):

    class Meta:
        model = NinethComment()
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()

class TenthCommentForm(forms.Form):
    
    class Meta:
        model = TenthComment()
        fields = (
            'text',
            'author',
        )

    text = forms.CharField()
    author = forms.CharField()