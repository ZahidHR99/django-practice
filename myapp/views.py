from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

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
        'html_content': '<strong>This is bold text</strong>',
        'none_value': None,
        'url': 'https://www.example.com',
        'email': '',
        'phone': '123-456-7890',
        'address': '123 Main St, Anytown, USA',
        'username': 'johndoe',
        'password': 'securepassword',
        'age': 28,
        'height': 5.9,
        'weight': 160,
        'is_active': True,
        'is_staff': False,
        'is_superuser': True,
        'date_joined': '2023-01-01',
        'last_login': '2023-06-01',
        'first_name': 'John',
        'last_name': 'Doe',
        'full_name': 'John Doe',
        'bio': 'This is a sample bio.',
        'profile_picture': 'path/to/profile.jpg',
        'website': 'https://www.johndoe.com',   
        'social_links': {
            'twitter': 'https://twitter.com/johndoe',
            'linkedin': 'https://linkedin.com/in/johndoe'
        },
        'skills': ['Python', 'Django', 'JavaScript'],
        'projects': [
            {'name': 'Project A', 'description': 'Description of Project A'},
            {'name': 'Project B', 'description': 'Description of Project B'},
            {'name': 'Project C', 'description': 'Description of Project C'}
        ],
        'hobbies': ['Reading', 'Traveling', 'Coding'],
        'favorite_color': 'Blue',
        'favorite_food': 'Pizza',
        'favorite_movie': 'Inception',
        'favorite_book': '1984',
        'favorite_music': 'Rock',
        'favorite_sport': 'Soccer',
        'favorite_place': 'Beach',
        'favorite_animal': 'Dog',
        'favorite_season': 'Spring',
        'favorite_quote': 'To be or not to be, that is the question.',
        'lucky_number': 7,
        'pi_value': 3.14159,
        'e_value': 2.71828,
        'golden_ratio': 1.61803,
        'is_happy': True,
        'is_sad': False,
        'is_excited': True,
        'is_bored': False,
        'is_tired': True,
        'is_stressed': False,
        'is_relaxed': True,
        'is_confused': False,
        'is_focused': True,
        'is_determined': True,
        'is_ambitious': True,
        'is_creative': True,
        'is_organized': True,
        'is_punctual': True,
        'is_reliable': True,
        'is_friendly': True,
        'is_helpful': True,
        'is_polite': True,
        'is_respectful': True,
        'is_honest': True,
        'is_loyal': True,
        'is_kind': True,
        'is_generous': True,
        'is_patient': True,
        'is_flexible': True,
        'is_adventurous': True,
        'is_curious': True,
        'is_open_minded': True,
        'is_empathetic': True,
        'is_compassionate': True,
        'is_grateful': True,
        'is_optimistic': True,
        'is_realistic': True,
        'is_critical': True,
        'is_analytical': True,
        'is_logical': True,
        'is_intuitive': True,
        'is_spontaneous': True,
        'is_methodical': True,
        'is_dedicated': True,
        'is_persistent': True,
        'is_resilient': False,
        'is_confident': True,
        'is_humble': True,
        'mydate': datetime.now(),
    }

    return render(request, 'about.html', data)

def contact(request):
    data = {
        'title': 'Contact Us',
        'user': {
            'is_authenticated': True,
            'is_anonymous': True,
            'id': 1,
            'username': 'admin',
            'is_active': True,
            'is_staff': False,
            'is_superuser': True,
            'date_joined': '2023-01-01',
            'last_login': '2023-06-01',
            'first_name': 'John',
            'last_name': 'Doe',
            'full_name': 'John Doe',
            'name': 'Jane Smith',
            'email': 'admin@gmail.com',
            'phone': '555-555-5555',
            'address': '456 Another St, Sometown, USA',
            'age': 32,
            'occupation': 'Manager',
            'company': 'Business Inc.',
            'website': 'https://www.janesmith.com',
            'social_links': {
                'twitter': 'https://twitter.com/janesmith',
                'linkedin': 'https://linkedin.com/in/janesmith'
            },
            'skills': ['Python', 'Django', 'JavaScript'],
            'hobbies': ['Photography', 'Traveling', 'Cooking'],
            'favorite_color': 'Green',
            'favorite_food': 'Sushi',
            'favorite_movie': 'The Matrix', 
            'favorite_book': 'To Kill a Mockingbird',
            'favorite_music': 'Jazz',
            'favorite_sport': 'Tennis',
            'favorite_place': 'Mountains',
            'favorite_animal': 'Lion',
            'favorite_season': 'Summer',
            'favorite_quote': 'The only way to do great work is to love what you do.',
            'lucky_number': 13,
            'pi_value': 3.14159,
            'e_value': 2.71828,
            'golden_ratio': 1.61803

        },
        'content': 'Welcome to the Contact Page',
    }

    return render(request, 'contact.html', data)

def products(request):
    return HttpResponse("This is the Products Page")

def services(request):
    return HttpResponse("This is the Services Page")

def blog(request):
    return HttpResponse("This is the Blog Page")

