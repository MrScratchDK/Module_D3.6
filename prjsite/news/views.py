from django.shortcuts import render
from .models import Post

def main(request):
    post = Post.objects.all()
    return render(request, 'main.html', context={'post': post})

def default(request, slug):
    new = Post.objects.get(slug__iexact=slug)
    return render(request, 'default.html', context={'new': new})