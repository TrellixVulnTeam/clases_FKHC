from django.urls import path     
from . import views
# http://127.0.0.1:8000/paciente
urlpatterns =[
    path('', views.index),
    path('listado', views.listado),
    path('plantillas', views.plantillaUno),
]