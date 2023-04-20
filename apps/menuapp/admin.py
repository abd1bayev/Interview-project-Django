from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from apps.menuapp.models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (MenuItemInline,)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'menu', 'parent', 'order')

    def url_link(self, obj):
        url = obj.url
        if url.startswith('/'):
            url = reverse('home') + url
        return format_html('<a href="{}">{}</a>', url, url)

    url_link.short_description = 'URL'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            if not request.resolver_match.args:
                return None
            menu_item_id = request.resolver_match.args[0]
            menu_item = MenuItem.objects.get(id=menu_item_id)
            kwargs['queryset'] = MenuItem.objects.filter(menu=menu_item.menu)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('menu').order_by('menu__name', 'order')
