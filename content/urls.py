from django.contrib import admin
from django.urls import path
from content.views import articles, article, category

app_name = 'content'

urlpatterns = [
    path("", articles, name="articles"),
    path("article/<int:id>", article, name="article"),
    path("category/<int:id>", category, name="category"),
]