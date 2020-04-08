from .models import *
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'ims/home.html')

# Get inventory list and display it
@login_required
def inventory(request):
    item_list = Item.objects.order_by('id')[:25]
    context = {'item_list': item_list,}
    return render(request, 'ims/inventory.html', context)

# Register for an account
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "ims/register.html", {"form":form})

def my_items(request):
    user = request.user
    my_item_list = Item.objects.filter(checked_to = user)
    context = {'my_item_list': my_item_list,}
    
    return render(request, 'ims/myitems.html', context)

def checkOut(request):
    instance = Item
    instance.checked_to = request.user
    instance.save()
    return 
def checkIn(request):
    instance = Item
    instance.checked_to = instance.checked_to(User="")
    instance.save()
    return 
