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
    path('insert_aeroporto', views.insert_aeroporto, name='insert_aeroporto'),

]
    