from django.db import models
from django.utils import timezone

# Create your models here.
class Airport(models.Model):
    identification = models.CharField(max_length=100, unique=True)
    type_airport = models.CharField(max_length=150)
    name =  models.CharField(max_length=200)
    latitude_deg = models.CharField(max_length=30)
    longitude_deg = models.CharField(max_length=30)
    elevation_ft = models.IntegerField()
    continent = models.CharField(max_length=100)
    iso_country = models.CharField(max_length=50)
    iso_region = models.CharField(max_length=50)
    municipality = models.CharField(max_length=100)
    gps_code = models.IntegerField()
    iata_code = models.CharField(max_length=30)
    local_code = models.CharField(max_length=30)
    cap = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=100)
    address_line_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Posto(models.Model):
    lettera = models.CharField(max_length=10)
    numero = models.IntegerField()
    volo = models.ForeignKey('Fly', on_delete=models.SET_NULL, null=True, default='Volo')

    def __str__(self):
        return self.lettera + self.numero
    
class Fly(models.Model):
    code_volo = models.CharField(max_length=200, unique=True)
    distanza_percorsa = models.IntegerField()
    ora_partenza = models.TimeField(auto_now=False, auto_now_add=False)
    ora_arrivo = models.TimeField(auto_now=False, auto_now_add=False)
    data_partenza = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    aeroporto_partenza = models.ForeignKey('Airport', on_delete=models.SET_NULL, related_name="a_partenza",default=-1,null=True)
    aeroporto_arrivo = models.ForeignKey('Airport', on_delete=models.SET_NULL, related_name="a_arrivo", default=-2,null=True)
    aircraft = models.ForeignKey('Aircraft', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code_volo

class Aircraft(models.Model):
    code_aircraft = models.CharField(max_length=100, unique=True)
    modello = models.CharField(max_length=200)
    stato = models.BooleanField()
    km_percorsi = models.IntegerField()
    posti_primaclasse = models.IntegerField()
    posti_secondaclasse = models.IntegerField()
    posti_economy = models.IntegerField()

    def __str__(self):
        return self.code_aircraft

class Personale(models.Model):
    STATUS = (
			('Volo', 'Volo'),
			('Assistenza', 'Assistenza'),
			('Terra', 'Terra'),
            ('Terra', 'Terra'),
			)
    code_personale = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mansione = models.CharField(max_length=200)
    ruolo = models.CharField(max_length=200, choices=STATUS)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    aircraft = models.ForeignKey('Aircraft', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code_personale

class Manutenzione(models.Model):
    ultima_manutenzione = models.DateTimeField(auto_now=False, auto_now_add=False)
    manutenzione_km  = models.IntegerField()
    manutenzione_giorni = models.IntegerField()
    km_restanti = models.IntegerField()
    aircraft = models.ForeignKey('Aircraft', on_delete=models.SET_NULL, null=True, )

    def __str__(self):
        return  self.ultima_manutenzione

class Utent(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    def __str__(self):
        return  self.lastname

class Prenotazione(models.Model):
    code_prenotazione = models.CharField(max_length=200, unique=True)
    utente = models.ForeignKey('Utent', on_delete=models.SET_NULL, null=True )
    volo = models.ForeignKey('Fly', on_delete=models.SET_NULL, null=True )
    posto = models.ForeignKey('Posto', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.code_prenotazione