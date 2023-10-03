from django.contrib import admin
from django.utils.html import format_html
from .models import event


@admin.register(event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date', 'theme', 'prix', 'pays', 'ville')
    list_filter = ('theme', 'date')
    search_fields = ('nom',)
    date_hierarchy = 'date'
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="event_images" width="50" height="50" />'.format(obj.image.url))

    image_tag.short_description = 'Image'



