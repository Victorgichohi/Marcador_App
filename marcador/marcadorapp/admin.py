from django.contrib import admin

from .models import Bookmark, Tag


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')#shows these fields
    list_editable = ('is_public',)#These fields are editable in the list view .
    list_filter = ('is_public', 'owner__username')#These fields can be filtered in the list view based on their values.
    search_fields = ['url', 'title', 'description']#These fields can be searched for in the list view based on their values
    readonly_fields = ('date_created', 'date_updated')#These fields are not editable in the detail view.


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
