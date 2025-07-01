from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .authentication import ArepUser
from .forms import ArepUserCreationForm

def registerView(request):
    if request.method == "post":
        form = ArepUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request,user)
            return redirect("dashboard")
    else:
        form = ArepUserCreationForm()
    return render(request,"accounts/register.html", {"form":form})

def index(request):
    return render(request,"accounts/index.html",{
        "title":"Bienvenue"
    })

def loginView(request):
    return render(request,"accounts/login.html",{
        "title":"Identification"
    })

def logoutView(request):
    logout(request)
    return redirect("login")

def myAccountView(request):
    title = "Mon compte utilisateur"
    user = request.user
    return render(request,"accounts/my-account.html",{
        "title":title,
        "user": user
    })

def addAccountView(request):
    title = "Nouvel utilisateur"
    return render(request,"accounts/add-account.html",{
        "title":title
    })

def accountList(request):
    title = "Comptes d'utilisateurs"
    users = ArepUser.objects.all
    return render(request,"accounts/account-list.html",{
        "title":title,
        "users":users
    })

def dashboardView(request):
    user = request.user
    if(user == None):
        return redirect("login")
    
    ac_data =  user.email if user.email else user.phone_number

    return render(request,"/accounts/dashboard.html",{
        "title": f"Welcome, {ac_data}",
        "user" : user
    })