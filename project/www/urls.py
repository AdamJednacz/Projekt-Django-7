from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_place/', views.add_place, name='add_place'),
    path('places/', views.places, name='places'),
    path('planing/', views.planing, name='planing'),
    path('trips/', views.trips, name='trips'),
    path('favorite/', views.favorite, name='favorite'),
    path('places/<int:place_id>/', views.places_detail, name='places_detail'),
]