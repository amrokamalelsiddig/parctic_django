from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"index.html")

def counter(request):
    textS = request.POST['name'] 
    number_of_words = len(textS.split())
    return render(request,"counter.html", { 'number_of_words':number_of_words})