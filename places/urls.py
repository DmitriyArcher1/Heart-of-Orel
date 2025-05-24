from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('', views.PlacesView.as_view(), name = 'places'),
    path('monument-to-tankmen/', views.FirstPlaceView.as_view(), name = 'first_place'),
    path('khimmashevsky-pond/', views.SecondPlace.as_view(), name = 'second_place'),
    path('saburovskaya-fortresse/', views.ThirdPlace.as_view(), name = 'third_place'),
    path('river-nepolod/', views.FourthPlace.as_view(), name = 'fourth_place'),
    path('tankers-square/', views.FifthPlace.as_view(), name = 'fifth_place'),
    path('children-park/', views.SixthPlace.as_view(), name = 'sixth_place'),
    path('gurtyev-square/', views.SeventhPlace.as_view(), name = 'seventh_place'),
    path('OGU/', views.EigthPlace.as_view(), name = 'eigth_place'),
    path('monument-to-ivan-the-terrible/', views.NinethPlace.as_view(), name = 'nineth_place'),
    path('monument-to-the-heroes-of-the-civil-war/', views.TenthPlace.as_view(), name = 'tenth_place'),
]
