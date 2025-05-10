from django.contrib import admin

from comment.models import Comment, EigthComment, FifthComment, NinethComment, SecondComment, SeventhComment, SixthComment, TenthComment, ThirdComment, FourthComment

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

@admin.register(FifthComment)
class FifthComment(admin.ModelAdmin):
    pass

@admin.register(SixthComment)
class SixthComment(admin.ModelAdmin):
    pass

@admin.register(SeventhComment)
class SeventhComment(admin.ModelAdmin):
    pass

@admin.register(EigthComment)
class EigthComment(admin.ModelAdmin):
    pass

@admin.register(NinethComment)
class NinethComment(admin.ModelAdmin):
    pass

@admin.register(TenthComment)
class TenthComment(admin.ModelAdmin):
    pass