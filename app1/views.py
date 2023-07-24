from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee>hello dhana when u get marry</marquee>')

def second(request):
    return HttpResponse('<h1><marquee>happy wedding aniversayday dhanna</h1>')
