from django.urls import path

from . import views

app_name = "ims"

urlpatterns = [
    path('', views.home, name="home"),
    path('inventory/', views.inventory, name='inventory'),
    path('myitems/', views.my_items, name='myitems'),
    path('reset-password/', views.reset_password, name='register'),
    
]

