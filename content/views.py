from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.urls import reverse
from content.models import Game, Author, Rating

# Create your views here.
def author(request, id):
    author=Author.objects.get(id=id)
    games= author.games.all()

    return render(request, 'content/author.html', {'author':author,'games':games})

def rating(request, id):
    rating=Rating.objects.get(id=id)
    games= rating.games.all()

    return render(request, 'content/rating.html', {'rating':rating,'games':games})

def game(request, id):
    game=Game.objects.get(id=id)

    return render(request, 'content/game.html', {'game': game})

def games(request):
    games=Game.objects.all()

    return render(request, 'content/games.html', {'games': games})
def homepage(request):
    return render(request, 'content/homepage.html')
def authors(request):
    authors=Author.objects.all()

    return render(request, 'content/authors.html', {'authors': authors})
def ratings(request):
    ratings=Rating.objects.all()

    return render(request, 'content/ratings.html', {'ratings': ratings})