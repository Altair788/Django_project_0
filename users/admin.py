from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'avatar',)  # Поля для отображения
    search_fields = ('email',)  # Поля для поиска
    list_filter = ('is_staff', 'is_active',)  # Фильтры для списка


admin.site.register(User, UserAdmin)
