from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuItem


def home(request):
    menus = Menu.objects.all()
    return render(request, 'home.html', {'menus': menus})


def menu(request, menu_name):
    menu = get_object_or_404(Menu, name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu, parent=None).order_by('order')
    context = {'menu': menu, 'menu_items': menu_items}
    return render(request, 'menu/menu.html', context)
