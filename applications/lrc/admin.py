# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local Folder
# Register your models here.
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        'email',
        'is_staff',
        'is_active',
        'is_manager',
    ]
    list_filter = ('email', 'is_staff', 'is_active', 'is_manager')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_manager')}),
        ('General', {'fields': ('first_name', 'last_name', 'avatar', 'groups')}),
    )
    add_fieldsets = (
        (
            None,
            {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')},
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.site_header = 'lrc admin panel'
