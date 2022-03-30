import re
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")

def acerca(request):
    return render(request, "core/acerca.html")

def tienda(request):
    return render(request, "core/tienda.html")

def categoria(request):
    return render(request, "core/categoria.html")