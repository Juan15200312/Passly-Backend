from django.contrib import admin
from Passwords.models import Pass


class PassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username', 'user', 'category')
    list_filter = ('category',)
    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__email',
        'password'
    )
    autocomplete_fields = ('user', 'category')
    ordering = ('id',)


admin.site.register(Pass, PassAdmin)