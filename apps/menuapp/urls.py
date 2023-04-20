from django.urls import path
from . import views


urlpatterns = [
    path('dwa/', views.home, name='home'),
    path('', views.geeks_view),

    path('menu/<str:menu_name>/', views.menu, name='menu'),
]
