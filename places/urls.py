from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('places/', views.PlacesView.as_view(), name = 'places')
]
