from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def carreras(request):
    return render(request,"core/carreras.html")

def docentes(request):
    return render(request,"core/docentes.html")