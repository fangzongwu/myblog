from django.contrib import admin
from .models import Category, TotalPrice

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'single_price']

class TotalPriceAdmin(admin.ModelAdmin):
	list_display = ['id', 'total', 'create_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(TotalPrice, TotalPriceAdmin)