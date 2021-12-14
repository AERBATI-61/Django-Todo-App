from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "selected_categories", "is_active", "is_home", "slug"]
    list_editable = ["is_active", "is_home"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    list_filter = ["title", "categories"]
    readonly_fields = ("slug",)

    def selected_categories(self, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        html += "</ul>"
        return mark_safe(html)


    class Meta:
        model = Article



class CommitAdmin(admin.ModelAdmin):
    readonly_fields = ("comment_content",)
admin.site.register(Comment, CommitAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ("slug",)
admin.site.register(Category, CategoryAdmin)
