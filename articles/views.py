from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.utils.text import slugify
from django.contrib import messages

def home(request):
    articles = Article.objects.all().order_by("-created_at")[:5]
    return render(request, "articles/home.html", {"articles": articles})

def index(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "articles/index.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})

@login_required
def create_article(request):
    # If the user submitted the form
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            return redirect(article.get_absolute_url())

    # If user is just opening the page
    else:
        form = ArticleForm()

    return render(request, "articles/create_article.html", {"form": form})

@login_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # Security check
    if article.author != request.user:
        return redirect(article.get_absolute_url())

    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.slug = slugify(article.title)
        article.save()

        return redirect(article.get_absolute_url())

    return render(request, "articles/edit_article.html", {"article": article})

@login_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if article.author != request.user:
        return redirect(article.get_absolute_url())

    if request.method == "POST":
        article.delete()
        return redirect("articles")

    return render(request, "articles/delete_article.html", {"article": article})

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            messages.success(request, "Article published successfully 🎉")
            return redirect(article.get_absolute_url())

    else:
        form = ArticleForm()

    return render(request, "articles/create_article.html", {"form": form})

@login_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if article.author != request.user:
        messages.error(request, "You are not allowed to edit this article.")
        return redirect(article.get_absolute_url())

    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()

        messages.success(request, "Article updated successfully ✨")
        return redirect(article.get_absolute_url())

    return render(request, "articles/edit_article.html", {"article": article})

@login_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if article.author != request.user:
        messages.error(request, "You cannot delete this article.")
        return redirect(article.get_absolute_url())

    if request.method == "POST":
        article.delete()
        messages.warning(request, "Article deleted 🗑️")
        return redirect("articles")

    return render(request, "articles/delete_article.html", {"article": article})