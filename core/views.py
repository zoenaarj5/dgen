from django.shortcuts import render

def index(request):
    return render(request,"core/home.html",{
        "title":"AREP, notre pilier"
    })