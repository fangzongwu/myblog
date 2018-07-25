from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, TotalPrice
from .serializers import CategorySerializer, TotalPriceSerializer

# 分类.
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

# 订单价格
class TotalPriceViewSet(viewsets.ModelViewSet):
	# ModelViewSet模型默认拥有get、post请求
	queryset = TotalPrice.objects.all().order_by('-create_date')
	serializer_class = TotalPriceSerializer

# 推荐美食
class CommendListViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.get_queryset().filter(is_commend=True)
	serializer_class = CategorySerializer

