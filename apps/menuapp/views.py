from django.shortcuts import render
from apps.menuapp.models import Menu


def home(request):
    menus = Menu.objects.values_list('name', flat=True)
    return render(request, 'home.html', {'menus': menus})

def menu(request, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        menu = None

    return render(request, 'menu/menu.html', {'menu': menu})
