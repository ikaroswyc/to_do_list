# -*- coding: utf-8 -*-
'''
@author: Yuchen Wang
@contact: ywang01@unomaha.edu
@software: Pycharm
@file: urls.py
@time: 9/30/18 10:10 PM
@desc:
'''

from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [

    path('home/', views.home, name = '主页'),
    path('about/', views.about, name = '关于'),
    path('edit/<i_id>', views.edit, name = '编辑'),
    path('del/<i_id>', views.delete, name = '删除'),
    path('cross/<i_id>', views.cross, name = '划掉'),
]