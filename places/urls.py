from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('', views.PlacesView.as_view(), name = 'places'),
    path('first_place/', views.FirstPlaceView.as_view(), name = 'first_place'),
]
