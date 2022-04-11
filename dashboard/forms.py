from dataclasses import field
from turtle import width
from django import  forms
from .models import *


class AirportForm(forms.ModelForm):
    class Meta:   
        model = Airport
        fields = '__all__'

class UtentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name', 'name': 'name'
    }))

    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name', 'name': 'lastname'
    }))

    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email', 'name': 'email'
    }))

    telefono = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Telefono', 'name': 'telefono'
    }))
    class Meta:
        model = Utent
        fields = '__all__'

class PostoForm(forms.ModelForm):
    lettera = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'name': 'lettera', 'id': 'lettera'
        }))
    numero = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class':'form-control', 'name':'numero', 'id': 'numero'
    }))

    classe = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'name': 'classe', 'id':'classe'
    }))


    class Meta:
        model = Posto
        fields = '__all__'


