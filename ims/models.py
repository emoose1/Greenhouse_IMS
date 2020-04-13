from django.db import models
from django.contrib.auth.models import User


#Category table, to hold possible category options for various items
class Category(models.Model): 
    category_name = models.CharField(max_length=100)
    category_slug= models.SlugField(max_length=100, unique=True)
    class Meta:
        #orders the category selection dropdown by category_name field
        ordering = ('category_name',)
        #sets the verbose name to "Category"
        verbose_name = 'Category'
        #sets the verbose plural name to "Categories", by default it would've been liseted as "Categorys"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name

#Item table, which holds all items and the item's fields
class Item(models.Model):
    
    #item_name is a  CharField to show if item is in or out of inventory
    item_name = models.CharField(max_length=200, verbose_name="Item Name")
    #item_status is a CharField that uses ITEM_STATUS_CHOICES as a choiceset to set the status of an item
    ITEM_STATUS_CHOICES = [('no', 'No'),('yes', 'Yes')]
    item_availability = models.CharField(max_length=3, choices=ITEM_STATUS_CHOICES, default='yes', verbose_name="Item Availability")
    #item_category uses foreign key from Category table
    item_category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE, verbose_name="Item Category")
    #item_uniqe_identifier is spefically for holding a serial number or service tag, if applicable
    item_unique_identifier = models.CharField(max_length=100, blank=True, null=True, verbose_name="Item Serial/Unique ID #")
    #item_specs is spefically for holding any specifications that might help distinguish an item
    item_specs = models.TextField(max_length=500, blank=True, null=True, verbose_name="Item Specs")
    #checked_out_date tracks the date and time an item was last checked out from the inventory
    checked_out_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    #checked_in_date tracks the date and time an item was last checked back into the inventory
    checked_in_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    #checked_to uses foreign key from User table
    checked_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Checked To User")

    class Meta:
        #orders any possible item selection dropdown by the item_name field
        ordering = ('item_name',)
        #sets the verbose name to "Item"
        verbose_name = 'Item'
        #sets the verbose plural name to "Items"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name
    #method for returning a short display of the item_specs field
    def snippetItemSpecs(self):
        if len(self.item_specs) > 0:
            return self.item_specs[:25] + "..."
        return self.item_specs
