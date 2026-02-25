from django.contrib import admin
from .models import SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'title', 'order')
    list_editable = ('order',)
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('admin_image',)
    ordering = ('order',)

    def admin_image(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html(
                '<img src="{}" style="width: 100px; height: auto;" />',
                obj.image.url
            )
        return '-'
    admin_image.short_description = 'Изображение'
