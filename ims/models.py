from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#Category table, to hold possible category options for various items
class Category(models.Model): 
    category_name = models.CharField(max_length=100)
    category_slug= models.SlugField(max_length=100, unique=True)
    class Meta:
        #orders the category selection dropdown by category_name field
        ordering = ('category_name',)
        
        verbose_name = 'Category'
       
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name

#Item table, which holds all items and the item's fields
class Item(models.Model):
    
    item_name = models.CharField(max_length=200, verbose_name="Item Name")   
    ITEM_STATUS_CHOICES = [('no', 'No'),('yes', 'Yes')]
    item_availability = models.CharField(max_length=3, choices=ITEM_STATUS_CHOICES, default='yes', verbose_name="Item Availability")   
    item_category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE, verbose_name="Item Category")  
    item_unique_identifier = models.CharField(max_length=100, blank=True, null=True, verbose_name="Item Serial/Unique ID #")
    item_specs = models.TextField(max_length=500, blank=True, null=True, verbose_name="Item Specs")
    date_added = models.DateTimeField(auto_now=True)
    checked_out_date = models.DateTimeField(auto_now=True, blank=True, null=True)   
    checked_in_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    checked_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Checked to Profile")

    class Meta:
        #orders any possible item selection dropdown by the item_name field
        ordering = ('item_name',)
       
        verbose_name = 'Item'
       
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name
    #method for returning a short display of the item_specs field
    def snippetItemSpecs(self):
        if len(self.item_specs) > 0:
            return self.item_specs[:25] + "..."
        return self.item_specs


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)

    def get_profile_items(self):
        return self.items.all()

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        user_profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)