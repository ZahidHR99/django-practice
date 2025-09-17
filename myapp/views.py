from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):

    data = {
        'title': 'About Us',
        'content': 'Welcome to the About Page',
        'number': 423.123123123,
        'list_items': ['Item 1', 'Item 2', 'Item 3'],
        'boolean': True,
        'list_dicts': [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 35}
        ],
        'mylist': [1, 2, 3, 4, 5],
        'html_content': '<strong>This is bold text</strong>'
    }

    return render(request, 'about.html', data)

def contact(request):
    return HttpResponse("This is the Contact Page")

def products(request):
    return HttpResponse("This is the Products Page")

def services(request):
    return HttpResponse("This is the Services Page")

def blog(request):
    return HttpResponse("This is the Blog Page")

