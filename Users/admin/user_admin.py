from django.contrib import admin
from Users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

    list_display_links = ('email', 'id')
    list_editable = ('is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('slug', 'last_login')
    fieldsets = (
        ('Credenciales de Acceso',
         {'fields': ('email', 'password'),
          }),
        ('Información Personal',
         {'fields': ('first_name', 'last_name',)
          }),
        ('Relaciones Internas', {
        'fields': ('info', 'slug', 'last_login'), 'classes': ('collapse',),
        'description': 'Metadatos autogenerados y relación OneToOne con Info.'}), ('Permisos y Seguridad', {
        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        'classes': ('collapse',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
