from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import context 
from django.db.models import Q
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *




# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request,'dashboard/dashboard.html')

@login_required(login_url='/login/')
def vista_aeroporti(request):
    ls_aeroporti = Airport.objects.all()
    context = {'aeroporti' : ls_aeroporti}
    return render(request, 'dashboard/aeroporti.html', context=context)

@login_required(login_url='/login/')
def insert_aeroporto(request):
    form = AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/aeroporti')        
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form}
    return render(request, 'dashboard/insert_aeroporto.html', context=context)


@login_required(login_url='/login/')
def update_aeroporto(request,pk):
    aeroporto = Airport.objects.get(id=pk)
    form = AirportForm(instance=aeroporto)
    if request.method == 'POST':
        form = AirportForm(request.POST, instance=aeroporto)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/aeroporti') 
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form,}
    return render(request,'dashboard/update_aeroporto.html', context)

@login_required(login_url='/login/')
def delete_aeroporto(request,pk):
    aeroporto = Airport.objects.get(id=pk)
    if request.method == 'POST':
        aeroporto.delete()
        return redirect('/dashboard/aeroporti') 
    else:
        messages.error(request, 'Errore')
    context = {'item' : aeroporto}
    return render(request, 'dashboard/delete_aeroporto.html', context)

@login_required(login_url='/login/')
def vista_voli(request):
    ls_voli = Fly.objects.all()
    context = {'voli' : ls_voli}
    return render(request, 'dashboard/voli.html', context=context)

@login_required(login_url='/login/')
def insert_volo(request):
    form = FlyForm()
    if request.method == 'POST':
        form = FlyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/voli')        
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form}
    return render(request, 'dashboard/insert_volo.html', context=context)

@login_required(login_url='/login/')
def update_volo(request,pk):
    volo = Fly.objects.get(id=pk)
    form = FlyForm(instance=volo)
    if request.method == 'POST':
        form = FlyForm(request.POST, instance=volo)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/voli') 
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form,}
    return render(request,'dashboard/update_volo.html', context)

@login_required(login_url='/login/')
def delete_volo(request,pk):
    volo = Fly.objects.get(id=pk)
    if request.method == 'POST':
        volo.delete()
        return redirect('/dashboard/voli') 
    else:
        messages.error(request, 'Errore')
    context = {'item' : volo}
    return render(request, 'dashboard/delete_volo.html', context)

@login_required(login_url='/login/')
def vista_prenotazioni(request):
    ls_prenotazioni = Prenotazione.objects.all()
    context = {'prenotazioni' : ls_prenotazioni}
    return render(request, 'dashboard/prenotazioni.html', context=context)

@login_required(login_url='/login/')
def insert_prenotazione(request):
    form = PrenotazioneForm()
    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/prenotazioni')        
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form}
    return render(request, 'dashboard/insert_prenotazione.html', context=context)

@login_required(login_url='/login/')
def update_prenotazione(request,pk):
    prenotazione = Prenotazione.objects.get(id=pk)
    form = PrenotazioneForm(instance=prenotazione)
    if request.method == 'POST':
        form = PrenotazioneForm(request.POST, instance=prenotazione)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/prenotazioni') 
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form,}
    return render(request,'dashboard/update_prenotazione.html', context)

@login_required(login_url='/login/')
def delete_prenotazione(request,pk):
    prenotazione = Prenotazione.objects.get(id=pk)
    if request.method == 'POST':
        prenotazione.delete()
        return redirect('/dashboard/prenotazioni') 
    else:
        messages.error(request, 'Errore')
    context = {'item' : prenotazione}
    return render(request, 'dashboard/delete_prenotazione.html', context)
