from ..models import Article, Category
from django import template

register = template.Library()




@register.simple_tag
def archives():
    return Article.objects.dates('add_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()