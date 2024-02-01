from django.contrib import admin
from django.http import HttpRequest

from news.models import News, Comment, Tag, Category


# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'view_count', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'category')
    readonly_fields = ('view_count', 'created_at', 'updated_at')
    fields = ('title', 'slug', 'content', 'is_active', 'category', 'tags', 'view_count', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}

    def has_add_permission(self, request: HttpRequest) -> bool:
        return True

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return True

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False


admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
