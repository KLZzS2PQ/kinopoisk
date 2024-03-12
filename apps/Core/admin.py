from django.contrib import admin

from apps.Core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar', 'is_staff',)
    list_editable = ('avatar', 'is_staff',)
