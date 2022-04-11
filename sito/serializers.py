from dataclasses import field
from rest_framework import serializers
from dashboard.models import *


class PostoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posto
        fields = '__all__'

class AirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AircraftSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlySerializers(serializers.ModelSerializer):
    aeroporto_partenza = AirportSerializers()
    aeroporto_arrivo = AirportSerializers()
    aircraft = AircraftSerializers()
    class Meta:
        model = Fly
        fields = '__all__'

class UtentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Utent
        fields = '__all__'

class PrenotazioneSerializers(serializers.ModelSerializer):
    utente = UtentSerializers()
    volo = FlySerializers()
    posto = PostoSerializers()
    class Meta: 
        model = Prenotazione
        fields = '__all__'

