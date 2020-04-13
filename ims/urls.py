from django.urls import path
from . import views as v

app_name = "ims"

urlpatterns = [
    path('', v.home, name="home"),
    path('inventory/', v.inventory, name='inventory'),
    path('myitems/', v.my_items, name='myitems'),
    path('reset-password/', v.reset_password, name='reset-password'),
    path('change-password/', v.change_password, name='change-password'),
]

