from django import forms

from comment.models import Comment, SecondComment, ThirdComment, FourthComment

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