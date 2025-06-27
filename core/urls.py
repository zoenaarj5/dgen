from django.urls import path
from .views import loginView,signupView,loginSuccessView,signupSuccessView, index

urlpatterns = [
    path("",index, name="index"),
    path("signup/",signupView, name="signup"),
    path("signup-success/<int:user_id>",signupSuccessView, name="signupSuccess"),
    path("login/",loginView, name="login"),
    path("login-success/<int:user_id>",loginSuccessView, name="loginSuccess"),
]