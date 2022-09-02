from datetime import datetime, timedelta
from time import strftime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from Registro.forms import FormRegistro
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    return render (request, "Registro/home.html")


@login_required
class FormRegistroV(HttpRequest):

    def index(request):
        register=FormRegistro()
        return render(request, "Registro/registro.html", {"form": register})
    
    def procesarform(request):
        register=FormRegistro(request.POST)
        if register.is_valid():
            register.save()
            register=FormRegistro()
        return redirect('pantalla')


def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form=AuthenticationForm()
    return render(request,"Registro/login.html",{"form":form})


def pantalla(request):
    dias = timedelta(days=3)
    fechaActual=datetime.today()
    fechaParticipacion=dias+fechaActual
    convertirFecha=fechaParticipacion.strftime('%d %b de %Y')
    return render(request, 'Registro/pantalla.html', {"Fecha":convertirFecha})


def cerrar_sesion(request):
    logout(request)
    return redirect('logear')


    
