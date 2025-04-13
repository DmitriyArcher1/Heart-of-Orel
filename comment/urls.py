from django.urls import path

from comment import views

app_name = 'comment'

urlpatterns = [
    path('first_place/', views.first_comments, name = 'comments'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
