from django.contrib import admin
from .models import Category, Item
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

admin.site.site_header = "Greenhouse IMS Admin"
admin.site.site_title = "Greenhouse IMS"
admin.site.index_title = "Greenhouse"

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs):

        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(label=("First Name"), max_length=50)
        self.fields['last_name'] = forms.CharField(label=("Last Name"), max_length=50)
        self.fields['email'] = forms.EmailField(label=("Email"), max_length=75)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('first_name','last_name','username','email','password1', 'password2')
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Item)