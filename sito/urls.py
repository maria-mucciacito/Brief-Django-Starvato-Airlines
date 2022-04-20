from os import name
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'prenotazione', views.PrenotazioneApi)
router.register(r'posto', views.PostoApi)
router.register(r'aeroporto', views.AirportApi)
router.register(r'volo', views.FlyApi)
router.register(r'aircraft', views.AircraftApi)
router.register(r'utent', views.UtentApi)


urlpatterns = [
    path('', views.index, name='home'),
    path('flights/',views.visualizza_voli, name="flights"),
    path('posto/<int:pk>/<int:adulti>/<str:classe>/<str:scelta>/',views.seleziona_posto , name='seleziona_posto'),
    path('imieivoli/', views.cerca_prenotazione, name='cerca_prenotazione'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api', include(router.urls)),
    path('riepilogo/', views.riepilogo, name='riepilogo'),
    path('prenotazione/', views.prenota, name='prenota'),
    path('imieivoli/delete/<int:id>/',views.cancella_prenotazione,name='cancella_prenotazione'),
]