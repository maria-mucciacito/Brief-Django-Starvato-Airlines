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

def insert_aeroporto(request):
    form = AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/aeroporti')        
        else:
            messages.error(request, 'Errore! Form non valido.')
    context = {'form': form}
    return render(request, 'dashboard/insert_aeroporto.html', context=context)
