from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    fields = ['news_title', 'content', 'photo', 'category', 'is_published']
    list_display = ('news_title', 'pub_date', 'category', 'get_photo', 'count_view', 'is_published')
    list_display_links = ('news_title', 'pub_date', 'category', 'count_view')
    list_filter = ['pub_date']
    search_fields = ('news_title', 'content')
    list_editable = ['is_published']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')


admin.site.register(News, NewsAdmin)


admin.site.register(Category)
