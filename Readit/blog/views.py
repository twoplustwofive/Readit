from django.shortcuts import render
from .models import Article
# Create your views here.

def Home(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'index.html',{'articles':articles})

def article_details(request,slug,id):
    article = Article.objects.get(pk=id)
    return render(request,'post.html',{'article':article})
