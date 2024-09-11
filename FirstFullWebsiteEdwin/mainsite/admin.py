from django.contrib import admin

# Register your models here.
from .models import User # import user

class UserAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('id', 'username', 'password', 'email', 'date_created', 'last_logged_in', 'name')
    # Optionally add search and filter options
    search_fields = ('username', 'email', 'name')
    list_filter = ('date_created', 'last_logged_in')

#Register the user model using UserAdmin
admin.site.register(User, UserAdmin)