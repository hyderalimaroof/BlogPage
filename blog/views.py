
from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Posts

# Create your views here.

posts = [
    {
        'title': 'hyder blog',
        'content': 'content of 1 blog',
        'date': '24:jan:2022',
    },
    {
        'title': 'haris blog',
        'content': 'content of 2 blog',
        'date': '31:Dec:2021',
    },
]


def home(request):
    content = {
        'posts': Posts.objects.all(),
        'title':'Home Blog'
    }
    return render(request, 'blog/home.html', content)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

def base (request):
    return render (request,'blog/base.html')
