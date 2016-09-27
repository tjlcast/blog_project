# -*- coding:utf-8 -*-
from django import template
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器，如8转为八
# @register.filter
# @register.filter(name='month_to_upper')
def month_to_upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'][key.month - 1]


def list_empty(l):
    if len(l) == 0:
        return True
    return False


def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))


register.filter('month_to_upper', month_to_upper)
register.filter('list_empty', list_empty)