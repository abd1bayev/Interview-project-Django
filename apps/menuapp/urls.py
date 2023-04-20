from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<str:menu_name>/', views.menu, name='menu'),
]
