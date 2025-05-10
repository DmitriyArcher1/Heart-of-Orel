from django.urls import path

from comment import views

app_name = 'comment'

urlpatterns = [
    # -------------------------------------------------------------------------
    path('first_place/', views.first_comments, name = 'first_comments'),
    path('second_place/', views.second_comments, name = 'second_comments'),
    path('third_place/', views.third_comments, name = 'third_comments'),
    path('fourth_place/', views.fourth_comments, name = 'fourth_comments'),
    path('fifth_place/', views.fifth_comments, name = 'fifth_comments'),
    path('sixth_place/', views.sixth_comments, name = 'sixth_comments'),
    path('seventh_place/', views.seventh_comments, name = 'seventh_comments'),
    path('eigth_place/', views.eigth_comments, name = 'eigth_comments'),
    path('nineth_place/', views.nineth_comments, name = 'nineth_comments'),
    path('tenth_place/', views.tenth_comments, name = 'tenth_comments'),
    # -------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------------------
    path('delete_first_comment/<int:comment_id>/', views.delete_first_comment, name = 'delete_first_comment'),
    path('delete_second_comment/<int:comment_id>/', views.delete_second_comment, name = 'delete_second_comment'),
    path('delete_third_comment/<int:comment_id>/', views.delete_third_comment, name = 'delete_third_comment'),
    path('delete_fourth_comments/<int:comment_id>/', views.delete_fourth_comments, name = 'delete_fourth_comments'),
    path('delete_fifth_comments/<int:comment_id>/', views.delete_fifth_comments, name = 'delete_fifth_comments'),
    path('delete_sixth_comments/<int:comment_id>/', views.delete_sixth_comments, name = 'delete_sixth_comments'),
    path('delete_seventh_comments/<int:comment_id>/', views.delete_seventh_comments, name = 'delete_seventh_comments'),
    path('delete_eigth_comments/<int:comment_id>/', views.delete_eigth_comments, name = 'delete_eigth_comments'),
    path('delete_nineth_comments/<int:comment_id>/', views.delete_nineth_comments, name = 'delete_nineth_comments'),
    path('delete_tenth_comments/<int:comment_id>/', views.delete_tenth_comments, name = 'delete_tenth_comments'),
    # ---------------------------------------------------------------------------------------------------------
]
