from django.urls import path
from . import views

urlpatterns = [
    path("members/",views.MemberView.as_view(),name="members"),
]