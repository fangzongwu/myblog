from rest_framework import serializers
from .models import Category, TotalPrice

# 分类
class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name', 'single_price', 'image', 'desc', 'is_commend')

# 订单价格
class TotalPriceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TotalPrice
		fields = ('id', 'total', 'create_date')