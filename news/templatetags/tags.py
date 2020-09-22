from django import template
from django.db.models.aggregates import *

from news.models import Category, News

register = template.Library()


@register.simple_tag
def list_categories():
    return Category.objects.filter(news__is_published=True).annotate(cnt=Count('news')).filter(cnt__gt=0)
