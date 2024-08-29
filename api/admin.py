from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import FriendRequest  # Import the FriendRequest model

# Get the User model
User = get_user_model()

# Customize the User admin interface (if using the default User model)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_staff')  # Customize fields to display
    search_fields = ('email',)  # Add a search bar by email
    ordering = ('id',)  # Order by ID

# Customize the FriendRequest admin interface
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'status', 'created_at')  # Customize fields to display
    list_filter = ('status', 'created_at')  # Add filter options in the admin panel
    search_fields = ('sender__email', 'receiver__email')  # Add a search bar by sender/receiver email

# Register your models with the admin site
admin.site.register(User, UserAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
