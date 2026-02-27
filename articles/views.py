from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all().order_by("-created_at")[:5]
    return render(request, "articles/home.html", {"articles": articles})

def index(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "articles/index.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})