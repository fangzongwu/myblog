from django.db import models

# Create your models here.
# 分类
class Category(models.Model):
	name = models.CharField(max_length=40)
	single_price = models.FloatField()

	def __str__(self):
		return self.name

# 订单
class TotalPrice(models.Model):
	total = models.FloatField()
	create_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.total