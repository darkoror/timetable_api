from django.contrib.auth.admin import UserAdmin

from user_profile.models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', )}),
        ('Important dates', {'fields': ('created_at',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'name', 'password1', 'password2',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('id', 'name', 'email', 'is_active')
    ordering = ('id',)
    list_filter = ()
    search_fields = ('email',)
    filter_horizontal = ()
    readonly_fields = ('created_at',)
