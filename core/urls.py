from django.urls import path
from .views import EmailOrPhoneLoginView,signupView,loginSuccessView,signupSuccessView, index

urlpatterns = [
    path("",index, name="index"),
    path("signup/",signupView, name="signup"),
    path("signup-success/<int:user_id>",signupSuccessView, name="signupSuccess"),
    path("login/",EmailOrPhoneLoginView.as_view(), name="login"),
    path("login-success/<int:user_id>",loginSuccessView, name="loginSuccess"),
]