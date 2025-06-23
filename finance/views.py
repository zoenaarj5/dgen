from django.shortcuts import render

def index(request):
    return render(request,"finance/home.html",{
        "title":"Finance homepage"
    }) 

def numbers(request):
    return render(request,"finance/numbers.html",{
        "title":"Finance numbers"
    })