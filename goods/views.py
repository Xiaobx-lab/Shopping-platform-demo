# -*- coding:utf-8 -*-
import json

from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from goods.models import *


class IndexView(View):
    def get(self, request, cid=2 , pageSize = 10, currentPage = 1):
        currentPage = request.GET.get('page')
        pageSize = request.GET.get('page_size')
        cid = int(cid)
        # 查询当前类别下的所有商品信息
        goodsList = Goods.objects.filter(category_id=cid).order_by('id')

        #分页（每页显示十条记录）
        pager = Paginator(goodsList, int(pageSize))

        #获取当前页的数据
        goodsList = pager.page(int(currentPage))

        data = []
        for goods in goodsList:
            goods_data = {
                "pageSize":pageSize,
                "currentPage":currentPage,
                "id": goods.id,
                "gname": goods.gname,
                "gdesc": goods.gdesc,
                "oldprice": goods.oldprice,
                "price": goods.price,
                "category": goods.category_id,
                "color_url": str(goods.getGimg()),
                "count": str(goods.getCount())
            }
            data.append(goods_data)

        return JsonResponse(data, safe=False, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})

# 每次访问的详情页面的商品id可以拿过来，我们存放到cookie里，只在客户端进行存储，并不在服务器端进行存储
def recommend_view(func):
    def wrapper(self, request,*args, **kwargs):
        goodsID = request.GET.get("id")
        # 获取cookie中的所有goodsID,如果没有就设置为空字符串
        goodsIDlistStr = request.COOKIES.get('recommend',' ')

        # 所有访问过得goodsID的列表
        goodsIDList = [gsID for gsID in goodsIDlistStr.split('-') if gsID.strip()]
        print('所有访问过得goodsID的列表',goodsIDList)
        # 推荐的商品GoodsObj列表 商品idList里对应的商品并且不能是当前浏览的，且必须和当前浏览的商品为同类
        goodsObjList = [Goods.objects.get(id=gsID) for gsID in goodsIDList if goodsID!= gsID and Goods.objects.get(id=goodsID).category_id==Goods.objects.get(id=gsID).category_id][:4]

        # 如果goodsID在goodsList中，则将原来列表中的ID删除，重新插入到最前面
        if goodsID in goodsIDList:
            goodsIDList.remove(goodsID)
            goodsIDList.insert(0,goodsID)
        else:
            goodsIDList.insert(0,goodsID)
        print('goodsIDList',goodsIDList)
        # 将goodsObjList传给get方法
        response = func(self,request,goodsID,goodsObjList,*args,**kwargs)
        # 将goodsID列表传递给cookie
        response.set_cookie('recommend','-'.join(goodsIDList),max_age =3*24*60*60)
        return response
    return wrapper

class Index(View):
    def get(self,request):
        return render(request, 'index.html')


class DetailView(View):
    @recommend_view
    def get(self, request, goodsID, goodsObjList=[]):

        goodsDetail = Goods.objects.get(id=goodsID)
        color_urls, color_names = goodsDetail.getImgs()

        recommend_list = []
        for goods in goodsObjList:
            goods_data = {
                "id": goods.id,
                "gname": goods.gname,
                "gdesc": goods.gdesc,
                "oldprice": goods.oldprice,
                "price": goods.price,
                "category": goods.category_id,
                "color_url": str(goods.getGimg()),
                "count": str(goods.getCount())
            }
            recommend_list.append(goods_data)
        data={
            "id": goodsDetail.id,
            "gname": goodsDetail.gname,
            "gdesc": goodsDetail.gdesc,
            "oldprice": goodsDetail.oldprice,
            "price": goodsDetail.price,
            "category_id": goodsDetail.category_id,
            "color_url": str(goodsDetail.getGimg()),
            "color_urls": color_urls,
            "color_names":color_names,
            "sizes":goodsDetail.getSizes(),
            "detailsList":goodsDetail.getDetailsList(),
            "recommend_list":recommend_list
        }
        print(recommend_list)
        # print(JsonResponse(data))
        return JsonResponse(data,safe=False, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})

