from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return  HttpResponse('<h1><marquee>ahalya when u get marry</h1>')
def second(request):
    return HttpResponse('<marquee>hello world')
