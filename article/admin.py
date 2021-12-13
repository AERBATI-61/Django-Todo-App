from django.contrib import admin

from .models import *
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author", "created_date", "is_active", "is_home", "slug"]
    list_editable = ["is_active", "is_home"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    readonly_fields = ("slug",)
    class Meta:
        model = Article



class CommitAdmin(admin.ModelAdmin):
    readonly_fields = ("comment_content",)
admin.site.register(Comment, CommitAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ("slug",)
admin.site.register(Category, CategoryAdmin)
