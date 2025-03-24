from django.urls import path

from comment import views

app_name = 'comment'

urlpatterns = [
    path('first_place/', views.first_comments, name = 'comments'),
]
