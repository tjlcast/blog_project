# -*- coding:utf-8 -*-
from django import template
register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器，如8转为八
# @register.filter
# @register.filter(name='month_to_upper')
def month_to_upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'][key.month - 1]


register.filter('month_to_upper', month_to_upper)