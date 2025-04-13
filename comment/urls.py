from django.urls import path

from comment import views

app_name = 'comment'

urlpatterns = [
    path('first_place/', views.first_comments, name = 'first_comments'),
    path('second_place/', views.second_comments, name = 'second_comments'),
    path('delete_first_comment/<int:comment_id>/', views.delete_first_comment, name = 'delete_first_comment'),
    path('delete_second_comment/<int:comment_id>/', views.delete_second_comment, name = 'delete_second_comment')
]
