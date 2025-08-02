from django.urls import path
from . import views

urlpatterns = [
    path("",views.news, name="indexNews"),
    path("news/",views.news, name="news"),
    path("article-detail/<int:article_id>",views.articleDetail, name="articleDetail"),
    path("add-article/",views.addArticle, name="addArticle"),
    path("edit-article/<int:article_id>",views.editArticle, name="editArticle"),
    path("forum/",views.forum, name="forum"),
]