from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("",views.index,name="home"),
    path("register/",views.registerView,name="register"),
    path("signin/",views.signinView,name="sign-in"),
    path("logged-user-detail/",views.loggedUserDetail,name="logged-user-detail"),
    path("request-new-password/",views.requestNewPasswordView,name="request-new-password"),
    path("edit-account/<int:user_id>",views.editAccountView,name="edit-account"),
    path("my-account/",views.myAccountView,name="my-account"),
    path("add-account/",views.addAccountView,name="add-account"),
    path("accounts/",views.accountList,name="accounts"),
    path("login/",views.loginView,name="login"),
    path("logout/",views.logoutView,name="logout"),
    path("dashboard/",views.registerView,name="dashboard"),

    path("registration/password-reset/",auth_views.PasswordResetView.as_view(),name="password-reset"),
    path("registration/password-reset/done/",auth_views.PasswordResetDoneView.as_view(),name="password-reset-done"),
    path("registration/reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(),name="password-reset-confirm"),
    path("registration/reset/done/",auth_views.PasswordResetCompleteView.as_view(),name="password-reset-complete"),
]