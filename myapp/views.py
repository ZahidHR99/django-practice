from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("This is the Contact Page")

def products(request):
    return HttpResponse("This is the Products Page")

def services(request):
    return HttpResponse("This is the Services Page")

def blog(request):
    return HttpResponse("This is the Blog Page")

