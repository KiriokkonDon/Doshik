from django.shortcuts import render
from.models import Articles

def index(request):
    data = {
        'title': 'Главная старница',
        'obj': {
            'Age': 'Age=18',
            'Hobby': 'Hobby=Game,Drawing',
            'Name': 'Name=Daria'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    Ff =Articles.objects.order_by('-date')
    return render(request, 'main/about.html', {'Ff': Ff})

