from django.shortcuts import render

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from . filters import GoodFilter

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import  filters
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

# class GoodListView(generics.ListAPIView):
#     """
#     商品列表Restful-API
#     """
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = StandardResultsSetPagination


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List:
        商品列表数据
    """
    queryset = GoodsCategory.objects.filter()#category_type=1)
    serializer_class = CategorySerializer