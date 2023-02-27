from django.contrib import admin
from . import models

# register the 'Item' model to the admin interface
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    # this specifies which fields should be displayed in the admin interface
    list_display = ('id', 'title')


# register the 'Order' model to the admin interface
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    # this specifies which fields should be displayed in the admin interface
    list_display = ('id', 'item')