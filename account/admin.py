from django.contrib import admin
from django.http import HttpRequest
from account.models import User, UserMessage, Groups
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    list_display_links = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'group_name']
    list_display_links = ['id', 'user_name', 'group_name']
    search_fields = ['user__username', 'group__name']


    def user_name(self, obj):
        return obj.user.username
    

    def group_name(self, obj):
        return obj.group.name
    

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    



@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    filter_horizontal = ['users']