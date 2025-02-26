from django.shortcuts import render
from .models import Post

posts = [
    {
        "title": "Blog post 1",
        "author": "Aman",
        "date_posted": "August 12",
        "content": "This is the first post",
    },
    {
        "title": "Blog post 2",
        "author": "ARaval",
        "date_posted": "August 12",
        "content": "This is the Second post",
    },
]


def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
