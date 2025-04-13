from django import forms

from comment.models import Comment, SecondComment

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