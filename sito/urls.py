from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('flights/',views.visualizza_voli, name="voli"),
    path('prenotazione/<str:pk>/<int:adulti>/<str:classe>/',views.seleziona, name='seleziona'),
    
]