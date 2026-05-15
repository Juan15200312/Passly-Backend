from django.contrib import admin

from Users.models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'user__is_active')
    list_display_links = ('id', 'get_user_name')

    fieldsets = (
        ('Contacto', {
            'fields': ('phone',),
        }),
        ('Información Personal', {
            'fields': ('birth_date', 'image'),
        }),
    )

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}" if hasattr(obj, 'user') else "---"

    get_user_name.short_description = 'Usuario'

admin.site.register(Info, InfoAdmin)