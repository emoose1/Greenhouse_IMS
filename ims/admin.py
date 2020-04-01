from django.contrib import admin

from .models import Inventory, Account, Item

admin.site.site_header = "Greenhouse IMS Admin"
admin.site.site_title = "Greenhouse IMS"
admin.site.index_title = "Greenhouse"

# admin.site.register(Inventory)
# admin.site.register(Account)

admin.site.register(Item)


class ItemInLine(admin.TabularInline):
    model = Item
    extra = 2

class AccountAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['name', 'email', 'user_account']}),]
    inlines = [ItemInLine]


admin.site.register(Account, AccountAdmin)