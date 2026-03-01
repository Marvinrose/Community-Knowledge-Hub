from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.shortcuts import redirect

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