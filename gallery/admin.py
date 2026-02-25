from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('admin_image', 'title', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('admin_image',)
    sortable = 'order'

    def admin_image(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html(
                '<img src="{}" style="width: 100px; height: auto;" />',
                obj.image.url
            )
        return '-'
    admin_image.short_description = 'Изображение'
