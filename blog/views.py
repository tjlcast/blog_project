# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.conf import settings # 读取setting信息
import logging

logger = logging.getLogger('blog.views')


def global_setting(request):
    return {'SITE_NAME' : settings.SITE_NAME,
            'SITE_DESC' : settings.SITE_DESC,
            }


# Create your views here.
def index(request):
    # 注意传入参数和render的参数
    try:
        file = open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())


def index2(request):
    try:
        pass
    except Exception as e:
        pass
    return render(request, 'new_index.html', locals())