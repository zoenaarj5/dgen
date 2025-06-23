from django.urls import path
from .views import loginView, index

urlpatterns = [
    path("",index, name="index"),
    path("login/",loginView, name="login"),
]