from django.shortcuts import render
from mypages.models import Home, About


def home_page(request):
    data = {
        'pages': Home.objects.all()
    }
    return render(request, 'home_page.html', data)


def about_me(request):
    data = {
        'pages': About.objects.all()
    }
    return render(request, 'about_me.html', data)