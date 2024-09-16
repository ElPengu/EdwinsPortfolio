from django.contrib import admin

# Register your models here.
from .models import todoListItem # import user

class todoListItemAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('id', 'user_id', 'title', 'description', 'completed', 'dateCreated', 'dateCompleted')

#Register the user model using UserAdmin
admin.site.register(todoListItem, todoListItemAdmin)
