from django.shortcuts import render
from django.shortcuts import redirect,render
from .forms import EmailOrPhoneLoginForms
from django.contrib.auth import authenticate,login

def index(request):
    return render(request,"core/home.html",{
        "title":"AREP, notre pilier"
    })

def loginView(request):
    form = EmailOrPhoneLoginForms(request.POST or None)
    if (request.method == "POST" and form.is_valid()):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate (request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            form.add_error(None, "Entrée invalide.")
    return render(request,"core/login.html",{"form":form})