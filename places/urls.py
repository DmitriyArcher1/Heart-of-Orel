from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('', views.PlacesView.as_view(), name = 'places'),
    path('first_place/', views.FirstPlaceView.as_view(), name = 'first_place'),
    path('second_place/', views.SecondPlace.as_view(), name = 'second_place'),
    path('third_place/', views.ThirdPlace.as_view(), name = 'third_place'),
    path('fourth_place/', views.FourthPlace.as_view(), name = 'fourth_place'),
    path('fifth_place/', views.FifthPlace.as_view(), name = 'fifth_place'),
    path('sixth_place/', views.SixthPlace.as_view(), name = 'sixth_place'),
    path('seventh_place/', views.SeventhPlace.as_view(), name = 'seventh_place'),
    path('eigth_place/', views.EigthPlace.as_view(), name = 'eigth_place'),
    path('nineth_place/', views.NinethPlace.as_view(), name = 'nineth_place'),
    path('tenth_place/', views.TenthPlace.as_view(), name = 'tenth_place'),

    # path('comments/tankers/', views.FirstComments.as_view(), name = 'first_comments'),
]
