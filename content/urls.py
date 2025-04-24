from django.contrib import admin
from django.urls import path
from content.views import author, game, games, rating, homepage, ratings, authors, login

app_name = 'content'

urlpatterns = [
    path("", homepage, name="homepage"),
    path("games", games, name="games"),
    path("ratings", ratings, name="ratings"),
    path("authors", authors, name="authors"),
    path("author/<int:id>", author, name="author"), 
    path("rating/<int:id>", rating, name="rating"), 
    path("game/<int:id>", game, name="game"),
    path("login", login, name="login"),
]