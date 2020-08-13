from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_case_posts(num=5):
     return Post.objects.filter(category_id=2)[:num]

@register.simple_tag
def get_recent_download_posts(num=5):
    return Post.objects.filter(category_id=4)[:num]

@register.simple_tag
def get_recent_information_posts(num=8):
    return Post.objects.filter(category_id=3)[:num]