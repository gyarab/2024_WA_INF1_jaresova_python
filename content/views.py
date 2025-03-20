from django.utils import timezone
from http.client import HTTPResponse
import json
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.forms import CommentForm
from content.models import Comment, Game, Author, Rating

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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            data = form.cleaned_data
            comment.name = data["name"]
            comment.text = data["text"]
            comment.game = game     
            comment.time = timezone.now()
            comment.ip = request.META['REMOTE_ADDR']
            comment.user_agent = request.META['HTTP_USER_AGENT']  
            comment.save()
            return HttpResponseRedirect(reverse('content:game', args=[id]))

    return render(request, 'content/game.html', {'game': game, 'form': form})

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