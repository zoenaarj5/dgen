from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="home"),
    path("register/",views.registerView,name="register"),
    path("my-account/",views.myAccountView,name="my-account"),
    path("add-account/",views.addAccountView,name="add-account"),
    path("accounts/",views.accountList,name="accounts"),
    path("login/",views.loginView,name="login"),
    path("logout/",views.logoutView,name="logout"),
    path("dashboard/",views.registerView,name="dashboard"),
]