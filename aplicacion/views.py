from django.shortcuts import render,redirect
from .models import Usuario
# Create your views here.

def home(request):
    usuario=Usuario.objects.all()
    return render(request, "mainpage.html",{"listados":usuario})

def registrar(request):
    frecuenciaC=request.POST['frecuenciaCardiaca']
    oxigenoS=request.POST['oxigenoSangre']
    estres=request.POST['estres']
    usuario=Usuario.objects.create(frecuenciaCardiaca=frecuenciaC,oxigenoSangre=oxigenoS,estres=estres)
    return redirect('/')