#自定义的模板标签
from django import template
from ..models import Post, Category

register = template.Library()

#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-create_time')[:num]


#归档模板标签
@register.simple_tag
def archives():
	return Post.objects.dates('create_time', 'month', order='DESC')


#分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()