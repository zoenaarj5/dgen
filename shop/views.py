from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to our shop !")

def shopHome(request, federation_id):
    return HttpResponse("This is the shopping home page.")
