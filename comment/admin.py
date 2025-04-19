from django.contrib import admin

from comment.models import Comment, SecondComment, ThirdComment, FourthComment

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

@admin.register(SecondComment)
class SecondComment(admin.ModelAdmin):
    pass

@admin.register(ThirdComment)
class ThirdComment(admin.ModelAdmin):
    pass

@admin.register(FourthComment)
class FourthComment(admin.ModelAdmin):
    pass