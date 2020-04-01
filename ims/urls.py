from django.urls import path

from . import views

app_name = "ims"

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('register/', views.register, name='register'),
]

