# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.conf import settings # 读取setting信息
from blog.models import Catagory # 读取分类信息
from blog.models import Article # 读取文章信息
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
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
        category_list = Catagory.objects.all()

        article_list = Article.objects.all()
        paginator = Paginator(article_list, 1) # 一页10条信息
        try:
            page = int(request.GET.get('page', 1)) # 当前页
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    # return render(request, 'new_index.html', {'category_list' : category_list})
    return render(request, 'new_index.html', locals())


def index_bak(request):
    return render(request, 'new_index_bak.html', locals())
