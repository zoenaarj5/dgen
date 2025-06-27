from django.shortcuts import render
from django.shortcuts import redirect,render, get_object_or_404
from .forms import EmailOrPhoneLoginForms,SignupForm
from django.contrib.auth import authenticate,login
from accounts.models import ArepUser

def index(request):
    return render(request,"core/home.html",{
        "title":"AREP, notre pilier"
    })

def signupView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = ArepUser.objects.create_user(
                email = form.cleaned_data["email"],
                phone_number = form.cleaned_data["phone_number"],
                password = form.cleaned_data["password"]
            )
            login(request,user)
            return redirect("signupSuccess",user_id=user.id)
    else:
        form = SignupForm()
        return render(request, "core/signup.html",{"form":form})

def signupSuccessView(request, user_id):
    user = get_object_or_404(ArepUser, id=user_id)
    return render("core/signup-success.html",{
        "user":user,
        "title":"Vous êtes enregistréé(e)!",
    })

def loginView(request):
    form = EmailOrPhoneLoginForms(request.POST or None)
    if (request.method == "POST" and form.is_valid()):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate (request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("loginSuccess",user_id=user.id)
        else:
            form.add_error(None, "Entrée invalide.")
    return render(request,"core/login.html",{"form":form})

def loginSuccessView(request,user_id):
    user = get_object_or_404(ArepUser,id=user_id)
    return render(request,"core/login-success.html",{
        "user":user,
        "title": "Vous êtes loggé(e)."
    })