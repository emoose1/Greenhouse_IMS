from django.shortcuts import render, redirect
from .models import Account, Inventory, Item
from .forms import RegisterForm

# Get inventory and display it
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

def logout(request):
    logout(request)