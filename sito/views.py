
from django.shortcuts import redirect, render
from django.template import context
from django.urls import is_valid_path
from django.views.generic.detail import DetailView
from markupsafe import re
from dashboard.models import *
from django.db.models import Q
from django.contrib import messages
from dashboard.forms import  PostoForm, UtentForm
from django.core.mail import BadHeaderError, send_mail
from rest_framework import viewsets
from .serializers import *

#Api rest
class PrenotazioneApi(viewsets.ModelViewSet):
    queryset = Prenotazione.objects.all()
    serializer_class = PrenotazioneSerializers

class PostoApi(viewsets.ModelViewSet):
    queryset = Posto.objects.all()
    serializer_class = PostoSerializers

class AirportApi(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializers

class FlyApi(viewsets.ModelViewSet):
    queryset = Fly.objects.all()
    serializer_class = FlySerializers

class AircraftApi(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializers

class UtentApi(viewsets.ModelViewSet):
    queryset = Utent.objects.all()
    serializer_class = UtentSerializers







# Create your views here.

def index(request):
    ls_airports = Airport.objects.all()
    context = {'aeroporti': ls_airports}
    return render(request, 'sito/index.html',context)

def visualizza_voli(request):
    context = {}
    if request.method == 'POST':
        aeroporto_partenza = request.POST['partenze']
        aeroporto_arrivo = request.POST['arrivi']
        data = request.POST['data']
        classe = request.POST['classe']
        adulti = request.POST['adulti']
        partenza = Airport.objects.get(city=aeroporto_partenza)
        arrivo = Airport.objects.get(city=aeroporto_arrivo)

        voli = Fly.objects.filter(Q(aeroporto_partenza=partenza.id) & Q(aeroporto_arrivo=arrivo.id) & Q(data_partenza=data))
        if (len(voli) == 0):
            context = {
            'voli': voli,
            'partenza': aeroporto_partenza,
            'arrivo' : aeroporto_arrivo,
            'data' : data,
            'classe': classe,
            'adulti': adulti,
            'message': 'Non ci sono voli disponibili!',
            }
        else:
            context = {
                'voli': voli,
                'partenza': aeroporto_partenza,
                'arrivo' : aeroporto_arrivo,
                'data' : data,
                'classe': classe,
                'adulti': adulti,
                'message': 'Ecco tutti i voli disponibili!',
            }

    else:
        messages.error(request, 'Errore!')
    
    return render(request,'sito/voli.html',context)

def seleziona_posto(request,pk,adulti,classe):
    volo = Fly.objects.get(id=pk)
    form_posto = PostoForm()
    form_utente = UtentForm()
   
        
    context = {
        'volo': volo,
        'classe': classe,
        'adulti': adulti,
        'form_posto': form_posto,
        'form_utente': form_utente
    }
    return render(request, 'sito/postieutente.html', context)

def cerca_prenotazione(request):
    prenotazioni = []
    if request.method == 'POST':
        code = request.POST['codice']
        name = request.POST['name']
        lastname = request.POST['lastname']
        utente = Utent.objects.filter(Q(name=name) & Q(lastname=lastname))
      

        prenotazioni = Prenotazione.objects.filter(Q(code_prenotazione=code) &  Q(utente=utente[0]))
        
        messages.success(request, 'Ecco tutte le tue prenotazioni')
        context = {
            'prenotazioni': prenotazioni,
        }

    else:
        messages.error(request, 'Non ci sono prenotazioni!')
    
    return render(request,'sito/imieivoli.html',context)



def riepilogo(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        telefono = request.POST['telefono']
        lettera = request.POST.get('lettera', '')
        numero = request.POST.get('numero', '')
        classet = request.POST.get('classe', '')
        id_volo = request.POST.get('id_volo', '')
        adulti = request.POST.get('adulti', '')
    
    
        volo = Fly.objects.get(id=id_volo)
        context = {
            'volo': volo,
            'name': name,
            'lastname': lastname,
            'email':email, 
            'telefono': telefono,
            'lettera': lettera,
            'numero': numero,
            'classe': classet,
            'adulti':adulti,
        }

    else:
        context['message'] = 'Errore!'

    return render(request, 'sito/prenotazione.html',context)

def prenota(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        telefono = request.POST['telefono']
        lettera = request.POST.get('lettera', '')
        numero = request.POST.get('numero', '')
        classet = request.POST.get('classe', '')
        id_volo = request.POST.get('id_volo', '')

        volo = Fly.objects.get(id=id_volo)
        utente = Utent(name=name, lastname=lastname, email=email, telefono=telefono)
        posto = Posto(lettera=lettera, numero=numero, classe = classet)
        posto.save()
        utente.save()
        prenotazione = Prenotazione(utente=utente, volo=volo, posto=posto)
        prenotazione.save()
        send_mail(
            'Conferma Prenotazione Starvato Airlines',
            'Gentile cliente la informiamo che la sua prenotazione è andata a buon fine. Le auguriamo buon viaggio! Cordiali saluti'+
            'Di seguito il codice della sua prenotazione : ' + prenotazione.code_prenotazione,
            'starvatoairlines@example.com',
            [email],
            fail_silently=False,
        ) 

        context = {
            'code_prenotazione' : prenotazione.code_prenotazione,
            'email': email,
        }
    else:
        context['message'] = 'Errore!'

    return render(request, 'sito/pagina_conferma.html', context)
        
    

            