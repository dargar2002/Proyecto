from django.urls import path
from .views import home, FormRegistroV
from .views import logear, cerrar_sesion, pantalla
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', logear, name="logear"),
    path('home', login_required(home), name="home"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('pantalla', pantalla, name='pantalla')
]