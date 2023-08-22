from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("<h1>Hola mundo - Desde Django 😊!</h1>")