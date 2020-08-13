import django_filters
from.models import *
class UsersFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤类
    """
    category = django_filters.NumberFilter(method='category_filter') #外键所以是numberfilter，category命名看前端
    author =django_filters.NumberFilter(method='author_filter')

    def author_filter(self,queryset,name,value):
        return queryset.filter(author_id=value)


    class Meta:
        model= User
        fields = ['id']