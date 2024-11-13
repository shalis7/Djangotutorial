from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def template(request):
    return render(request, 'index.html')