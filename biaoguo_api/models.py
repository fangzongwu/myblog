from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=40)
	single_price = models.FloatField()

	def __str__(self):
		return self.name
