from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'tg_username', 'tg_id', 'is_subscribe', 'pk',)
