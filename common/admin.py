from django.contrib import admin
from common.models import Media, FAQ, Advertising
# Register your models here.


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']
    search_fields = ['id']
    list_filter = ['type']
    


admin.site.register(FAQ)
admin.site.register(Advertising)