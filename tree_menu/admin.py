from django.contrib import admin

from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'url', 'order')
    list_filter = ('menu_name',)
    search_fields = ('name', 'url')
    ordering = ('menu_name', 'order')
    list_editable = ('order',)


admin.site.register(MenuItem, MenuItemAdmin)
