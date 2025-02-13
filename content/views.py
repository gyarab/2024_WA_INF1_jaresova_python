from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.urls import reverse
from content.models import Game, Category

# Create your views here.
def category(request, id):
    category=Category.objects.get(id=id)
    games= category.games.all()

    return render(request, 'content/category.html', {'category':category,'games':games})

def game(request, id):
    game=Category.objects.get(id=id)

    return render(request, 'content/game.html', {'game': game})

def games(request):
    games=Category.objects.all()

    return render(request, 'content/games.html', {'games': games})

def companies(request):
    companies=Category.objects.all()

    return render(request, 'content/companies.html', {'companies': companies})