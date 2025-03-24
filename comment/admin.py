from django.contrib import admin

from comment.models import Comment

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass