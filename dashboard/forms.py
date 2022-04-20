from dataclasses import field, fields
from pyexpat import model
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

class FlyForm(forms.ModelForm):

    data_partenza = forms.DateField( widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    ora_partenza = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time'
    }))
    ora_arrivo = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time'
    }))
    class Meta:   
        model = Fly
        fields = '__all__'

class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = '__all__'