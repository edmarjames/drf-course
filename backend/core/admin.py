from django.contrib import admin
from .models import Contact

# decorator to register the Contact model to the admin interface
@admin.register(Contact)

# this class is used to customize the behavior of the admin interface for the contact model
class ContactAdmin(admin.ModelAdmin):
    # this specifies which fields should be displayed in the list of contacts in the admin interface
    list_display = ('id', 'title', 'description', 'email')