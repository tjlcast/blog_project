# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.conf import settings # 读取setting信息
from blog.models import Catagory # 读取分类信息
from blog.models import Article # 读取文章信息
from blog.models import Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
import logging

logger = logging.getLogger('blog.views')


def global_setting(request):
    return {'SITE_NAME' : settings.SITE_NAME,
            'SITE_DESC' : settings.SITE_DESC,
            }


# Create your views here.

def index(request):
    try:
        category_list = Catagory.objects.all()

        article_list = Article.objects.all()
        paginator = Paginator(article_list, 1) # 一页10条信息
        try:
            page = int(request.GET.get('page', 1)) # 当前页
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)

        # 文章归档
        # 1, 先去获取到文章中有的 年份和月份

        # 2,
    except Exception as e:
        logger.error(e)
    # return render(request, 'new_index.html', {'category_list' : category_list})
    return render(request, 'index.html', locals())


def index_bak(request):
    return render(request, 'new_index_bak.html', locals())


# 文章详情
def article(request):

    if request.method == 'POST':  # 如果表单被提交
        form = CommentForm(request.POST)  # 获取Post表单数据
        print form


    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)

        comment_form = CommentForm({
            'author' : request.user.username,
            'email' : request.user.email,
            'url' : request.user.url,
            'article' : id
        } if request.user.is_authenticated() else {'article' : 'id'})

        # comment_list = article.comment_set.all()
        comments = Comment.objects.filter(article=article).order_by('id')
        comment_list = []
        for comment in comments:
            for item in comment_list:
                    if not hasattr(item, 'children_comment'): # 临时为一个评论对象增加一个子评论集合
                        setattr(item, 'children_comment', [])
                    if comment.pid == item:
                        item.children_comment.append(comment)
                        break
            if comment.pid is None:
                comment_list.append(comment)
    except Exception as e:
        return render(request, 'failure.html', {'reason' : '没有找到对应的文章'})
    return render(request, 'article_old.html', locals())


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        pass
    else:
        # Return an 'invalid login' error message.
        pass
    render(request, 'login.html', locals())

