from django.contrib import admin
from django.urls import path
from content.views import category, game, games, companies

app_name = 'content'

urlpatterns = [
    path("", games, name="games"),
    path("category/<int:id>", category, name="category"), 
    path("game/<int:id>", game, name="game"),
    path("companies", companies, name="companies"),
]