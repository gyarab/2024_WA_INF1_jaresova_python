from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.urls import reverse
from content.models import Article

# Create your views here.
def articles(request):
    articles=Article.objects.all()

    return render(request, 'content/articles.html', {'articles': articles})
    
def article(request, id):
    article=Article.objects.get(id=id)

    return render(request, 'content/article.html', {'article': article})
