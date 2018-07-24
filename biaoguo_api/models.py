from django.db import models

# Create your models here.
# 分类
class Category(models.Model):
	name = models.CharField(max_length=40)
	single_price = models.FloatField()
	image = models.CharField(max_length=200, null=True, blank=True)
	desc = models.CharField(max_length=100, null=True, blank=True)
	is_commend = models.BooleanField()


	def __str__(self):
		return self.name

# 订单
class TotalPrice(models.Model):
	total = models.FloatField()
	create_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.total