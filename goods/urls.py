#coding=utf-8

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns=[
    url(r'^api/goodsDetail/', views.DetailView.as_view()),
    url(r'^$', views.IndexView.as_view()),
]