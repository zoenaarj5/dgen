from django.urls import path
from . import views

urlpatterns = [
    path("",views.news, name="indexNews"),
    path("news/",views.news, name="news"),
    path("forum/",views.forum, name="forum"),
]