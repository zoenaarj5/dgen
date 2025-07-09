from django.shortcuts import render


def news(request):
    return render(request,"blog/news.html",{
        "title":"Latest news"
    })

def forum(request):
    return render(request,"blog/forum.html",{
        "title":"La parole est à vous"
    })