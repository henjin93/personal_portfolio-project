from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles' : articles})