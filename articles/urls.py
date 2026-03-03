from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="articles"),      # /articles/
    path("new/", views.create_article, name="create_article"),
    path("<slug:slug>/edit/", views.edit_article, name="edit_article"),
    path("<slug:slug>/delete/", views.delete_article, name="delete_article"),
    path("<slug:slug>/", views.article_detail, name="article_detail"),  # ALWAYS LAST
]