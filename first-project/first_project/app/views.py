import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime



def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = str(datetime.time(datetime.now()))
    msg = f'Текущее время: {current_time[:-7]}'
    return HttpResponse(msg)


def workdir_view(request):
    directory = os.listdir("app")
    msg = f'Рабочая директория седержит: {directory}'
    return HttpResponse(msg)
