from django.shortcuts import render

def index(request):
    return render(request,"blog/home.html",{
        "title":"Welcome to our blog"
    })
def news(request):
    return render(request,"blog/news.html",{
        "title":"Latest news"
    })