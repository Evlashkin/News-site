from django.contrib import admin

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    fields = ['news_title', 'content', 'photo', 'category', 'is_published']
    list_display = ('news_title', 'pub_date', 'category', 'count_view', 'is_published')
    list_display_links = ('news_title', 'pub_date', 'category', 'count_view')
    list_filter = ['pub_date']
    search_fields = ('news_title', 'content')
    list_editable = ['is_published']


admin.site.register(News, NewsAdmin)


admin.site.register(Category)
