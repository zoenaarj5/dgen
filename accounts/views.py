from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .authentication import ArepUser
from django.db import transaction
from .forms import ArepUserCreationForm,LoginForm,ArepUserEditForm

def registerView(request):
    if request.method == "post":
        user_form = ArepUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit = False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            login(request,user)
            return redirect("dashboard")
    else:
        user_form = ArepUserCreationForm()
    return render(request,"accounts/register.html", {"user_form":user_form})

def index(request):
    return render(request,"accounts/index.html",{
        "title":"Bienvenue"
    })

def editAccountView(request,user_id):
    
    title="Modification de compte (admin)"

    if(request.method=="POST"):
        user_form=ArepUserEditForm(request.POST)
        if(user.form.is_valid()):
            with transaction.atomic():
                user=user_form.save(commit=False)
                user.set_password(user_form.cleaned_data.password)
                user.save()
                return redirect(f"/accounts/user-detail/{user.id}")
    else:
        user_form=ArepUserEditForm()

    context={
        "title":title,
        "user_form":user_form
    }
    return render(request,"accounts/edit-account.html",context)

def loginView(request):
    form = LoginForm(request.POST or None)
    error=None
    if(request.method == "POST"):
        if(form.is_valid()):
            username=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user = authenticate(request, username=username,password=pwd)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                error = "Utilisateur non valide."
    return render(request,"accounts/login.html",{
        "form":form,
        "error":error,
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

def loggedUserDetail(request):
    logged_user = request.user
    title="Utilisateur connecté"
    return render(request,"logged-user-detail.html",{
        "logged_user":logged_user,
        "title":title
    })

def signinView(request):
    logout(request)
    title = "Entrez par ici"
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("logged-user-detail")
#    else:
    form = LoginForm()
    return render(request,"accounts/signin.html",{
        "title":title,
        "signin_form":form
    })

def requestNewPasswordView(request):
    if(request.method == "POST"):
        pass
    else:
        title = "Demander un nouveau mot de passe"
        message = "Veuillez entrer votre email, un code vous sera envoyé pour réinitialiser votre mot de passe."
        return render(request,"accounts/request-new-password.html",{
            "title":title,
            "message":message
        })