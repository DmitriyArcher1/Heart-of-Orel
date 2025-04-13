from django.contrib import admin

from comment.models import Comment, SecondComment

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

@admin.register(SecondComment)
class SecondComment(admin.ModelAdmin):
    pass