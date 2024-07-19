from django.contrib import admin
from news.models import News, NewsImage
from django.contrib.auth.models import User, Group
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    search_fields = ['id']
    

admin.site.unregister(User)
admin.site.unregister(Group)