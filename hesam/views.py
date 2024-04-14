from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'website/index.html')


def blog(request):
    return render(request, 'website/blog.html')


def info(request):
    return render(request, 'website/info.html')
