from django import template

from news.models import Category, News

register = template.Library()


@register.simple_tag
def list_categories():
    return Category.objects.all()
