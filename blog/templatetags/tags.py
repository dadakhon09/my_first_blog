from django import template

from blog.models import Tag

register = template.Library()


@register.simple_tag(name='tags')
def asd():
    return Tag.objects.all()
