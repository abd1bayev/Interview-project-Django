from django.shortcuts import render
from apps.menuapp.models import Menu


def home(request):
    return render(request, 'home.html')

def menu(request, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        menu = None

    return render(request, 'menu/menu.html', {'menu': menu})


def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)