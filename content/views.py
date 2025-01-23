from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def articles(request):
    with open('articles.json', encoding="utf-8") as file:
        data =json.load(file)

        return render(request, 'content/articles.html', {'data': data})

        
    
def article(request, id):
    with open("articles.json", encoding="utf-8") as file:
        data = json.load(file)
        article = data[id]
        return render(request, 'content/article.html', {'article': article})
