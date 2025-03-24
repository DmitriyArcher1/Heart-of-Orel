from django import forms

from comment.models import Comment

class CommentForm(forms.Form):

    class Meta:
        model = Comment
        fields = (
            'text',
            'author',
        )
    
    text = forms.CharField()
    author = forms.CharField()