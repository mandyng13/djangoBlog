from django.shortcuts import render
from django.http import HttpResponse

# dummy database
posts = [
    {
        'author': 'Mandy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 15, 2025'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 16, 2025'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

