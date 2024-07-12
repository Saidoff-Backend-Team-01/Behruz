from django.contrib import admin
from news.models import News
from django.contrib.auth.models import User, Group
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    

admin.site.unregister(User)
admin.site.unregister(Group)