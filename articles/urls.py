from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.index, name="articles"),   # homepage
    path("articles/new/", views.create_article, name="create_article"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
]