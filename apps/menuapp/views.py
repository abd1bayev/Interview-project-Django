from django.shortcuts import render, get_object_or_404
from .models import Menu


def home(request):
    menus = Menu.objects.values_list('name', flat=True)
    return render(request, 'home.html', {'menus': menus})


def menu(request, menu_name):
    menu = get_object_or_404(Menu, name=menu_name)

    return render(request, 'menu/menu.html', {'menu': menu})
