# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.

def index(request):
    # 注意传入参数和render的参数
    return render(request, 'index.html', locals())