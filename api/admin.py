from django.contrib import admin

from .models import TemplateItem


@admin.register(TemplateItem)
class TemplateItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_id', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'description')
