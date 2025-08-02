from django.shortcuts import get_object_or_404, render, redirect
from .models import Article
from .forms import ArticleForm
from django.db import transaction

def addArticle(request):
    title="New article"
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            with transaction.atomic():
                article = article_form.save()
                article.author=request.user
                article.save()
                return redirect(f"/blog/article-detail/{article.id}")
    else:
        article_form = ArticleForm()

    return render(
        request, "blog/add-article.html",{
        "title":"Ajout nouvel article",
        "article_form":article_form
    }) 

def editArticle(request,article_id):
    title=" article"
    article = get_object_or_404(Article,id=article_id)
    if request.method == "POST":
        article_form = ArticleForm(request.POST,instance=article)
        if article_form.is_valid():
            with transaction.atomic():
                article = article_form.save()
                article.save()
                return redirect(f"/blog/article-detail/{article.id}")
    else:
        article_form = ArticleForm(instance=article)

    return render(
        request, "blog/edit-article.html",{
        "title":f"Modifier l'article \"{article.title}\"",
        "article_form":article_form
    }) 

def articleDetail(request,article_id):
    article=get_object_or_404(Article,id=article_id)
    return render(request,"blog/article-detail.html",{
        "title":f"Article #{article.id} - \"{article.title}\"",
        "article":article
    })

def news(request):
    articles=Article.objects.all
    return render(request,"blog/news.html",{
        "title":"Latest news",
        "news":articles
    })

def forum(request):
    return render(request,"blog/forum.html",{
        "title":"La parole est à vous"
    })