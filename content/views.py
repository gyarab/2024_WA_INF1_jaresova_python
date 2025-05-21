from django.utils import timezone
from http.client import HTTPResponse
import json
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from content.forms import CommentForm, LoginForm, RegisterForm, LogoutForm
from content.models import Comment, Game, Author, Rating
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


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
            if request.user.is_authenticated:
                comment.name = request.user.username
            elif data["name"]:
                comment.name = data["name"]
            else:
                comment.name = "Anonymous"
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('content:homepage'))
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'content/login.html', {'form': form, 'user': request.user})
    else:
        form = LoginForm()
        return render(request, 'content/login.html', {'form': form, 'user': request.user})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('content:homepage')) 

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'content/register.html', {'register_form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                form.add_error('password2', 'The two password fields don\'t match.')
                return render(request, 'content/register.html', {'register_form': form})

            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
            except IntegrityError:
                form.add_error('username', 'This username is already taken.')
                return render(request, 'content/register.html', {'register_form': form})

            return redirect('content:login')
        else:
            return render(request, 'content/register.html', {'register_form': form})            


def my_view(request):
    if request.user.is_authenticated:
        user = request.user
        name = user.get_full_name()
        return HttpResponseRedirect(reverse('content:login'))
