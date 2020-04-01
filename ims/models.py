from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    user_account = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    item_text = models.CharField(max_length=200)
    item_status = models.BooleanField(default=True)
    item_specs = models.CharField(max_length=200)
    checked_out_date = models.DateTimeField(auto_now=True)
    checked_in_date = models.DateTimeField(auto_now=True)
    checked_to = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_text

class Inventory(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete= models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.inventory_text