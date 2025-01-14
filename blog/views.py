from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

#function based view

#def home(request):
#    return render(request, 'home.html', {})

# class based view

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'