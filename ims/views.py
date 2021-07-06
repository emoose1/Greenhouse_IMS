from .models import *
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'ims/home.html')

# Get inventory list and display it
@login_required(login_url='login')
def inventory(request):
    item_list = Item.objects.order_by('id')[:25]
    context = {'item_list': item_list,}
    
    return render(request, 'ims/inventory.html', context)

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/login')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change-password.html', args)

def reset_password(response):
    if response.method == "POST":
        form = PasswordResetForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = PasswordResetForm()
    return render(response, "registration/reset-password.html", {"form":form})

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def my_items(request):
    my_user = request.user
    my_item_list = Item.objects.filter(checked_to = my_user)
    context = {'my_item_list': my_item_list,}
    
    return render(request, 'ims/myitems.html', context)


@login_required(login_url='login')
def checkIn(request):
    item_instance = Item
    item_instance.checked_to = item_instance.checked_to(user=request.user)
    item_instance.save()
    return

@login_required()
def add_to_checkOut(request, **kwargs):
    
    return
