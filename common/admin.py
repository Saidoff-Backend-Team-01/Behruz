from django.contrib import admin
from common.models import Media
# Register your models here.


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']