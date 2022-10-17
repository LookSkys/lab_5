from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse ("<h1>Informatica USM</h1><hr><nav><lu><li><a href="{% url'home'%}">Home</a></li><li><a href="{% url'carreras'%}">Carreras</a></li><li><a href="{% url'docentes'%}">Docentes</a></li></lu></nav><hr><h3>lorem</h3>")

def carreras(request):
    return HttpResponse("<h1>Carreras</h1><hr><h2>Menu</h2><hr><h3>lorem<h3>")

def docentes(request):
    return HttpResponse("<h1>Docentes</h1><hr><h2>Menu</h2><hr><h3>lorem<h3>")