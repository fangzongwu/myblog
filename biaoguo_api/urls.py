from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'categories', views.CategoryViewSet)
router.register(r'total_price', views.TotalPriceViewSet)
router.register(r'commend_list', views.CommendListViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]
