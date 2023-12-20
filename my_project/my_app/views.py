from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'title': 'Home',
        'heading': 'Welcome to my website',
        'content': 'This is the content of my website'
    }
    return render(request,"index.html", context)