from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.urls import reverse
from content.models import Article, Category

# Create your views here.
def articles(request):
    articles=Article.objects.all()

    return render(request, 'content/articles.html', {'articles': articles})
    
def article(request, id):
    article=Article.objects.get(id=id)

    return render(request, 'content/article.html', {'article': article})

def category(request, id):
    category=Category.objects.get(id=id)
    articles= category.articles.all()

    return render(request, 'content/category.html', {'category':category,'articles':articles})

def game(request, id):
    game=Category.objects.get(id=id)

    return render(request, 'content/game.html', {'game': game})

def games(request):
    games=Category.objects.all()

    return render(request, 'content/games.html', {'games': games})

def companies(request):
    companies=Category.objects.all()

    return render(request, 'content/companies.html', {'companies': companies})