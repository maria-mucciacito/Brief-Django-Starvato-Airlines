from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login' ),
    path('logout/',auth_views.LogoutView.as_view(),name='logout' ),
    path('dashboard/',views.index, name='index'),
    path('dashboard/aeroporti/', views.vista_aeroporti, name='aeroporti'),
    path('dashboard/aeroporti/insert_aeroporto', views.insert_aeroporto, name='insert_aeroporto'),
    path('dashboard/aeroporti/update_aeroporto/<str:pk>/', views.update_aeroporto, name='update_aeroporto'),
    path('dashboard/aeroporti/delete_aeroporto/<str:pk>/', views.delete_aeroporto, name='delete_aeroporto'),
    path('dashboard/voli/', views.vista_voli, name='voli'),
    path('dashboard/voli/insert_volo',views.insert_volo,name='insert_volo'),
    path('dashboard/voli/update_volo/<str:pk>/', views.update_volo, name='update_volo'),
    path('dashboard/voli/delete_volo/<str:pk>/', views.delete_volo, name='delete_volo'),
    path('dashboard/prenotazioni/',views.vista_prenotazioni, name='prenotazioni'),
    path('dashboard/prenotazioni/insert_prenotazione/', views.insert_prenotazione, name='insert_prenotazione'),
    path('dashboard/prenotazioni/update_prenotazione/<str:pk>/',views.update_prenotazione,name='update_prenotazione'),
    path('dashboard/prenotazioni/delete_prenotazione/<str:pk>/',views.delete_prenotazione, name='delete_prenotazione'),

]
    