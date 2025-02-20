from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('', views.PlacesView.as_view(), name = 'places'),
    path('first_place/', views.FirstPlaceView.as_view(), name = 'first_place'),
    path('second_place/', views.SecondPlace.as_view(), name = 'second_place'),
    path('third_place/', views.ThirdPlace.as_view(), name = 'third_place'),
    path('fourth_place/', views.FourthPlace.as_view(), name = 'fourth_place'),
]
