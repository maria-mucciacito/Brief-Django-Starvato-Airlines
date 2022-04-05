 from django.forms import ModelForm
from .models import *

class AirportForm(ModelForm):
    class Meta:   
        model = Airport
        fields = '__all__'