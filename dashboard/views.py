from django.shortcuts import render
from django.contrib import messages
from django.template import context 
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request,'dashboard/dashboard.html')
