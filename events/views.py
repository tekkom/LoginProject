from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("Herro WORDL")
    return render(request, 'index.html')
