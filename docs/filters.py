import django_filters
from.models import Doc
from django.db.models import Q
class DocsFilter(django_filters.rest_framework.FilterSet):
    """
    文档过滤类
    """
    top_doc = django_filters.NumberFilter(method='top_doc_filter') #外键所以是numberfilter

    #根据top_doc过滤一级非删除状态文档
    def top_doc_filter(self,queryset,name,value): #默认传递参数,value=top_doc.id
       return queryset.filter(~Q(status=3),top_doc_id=value,parent_doc=None) #关键字参数必须在位置参数Q后面

    class Meta:
        model= Doc
        fields = ['top_doc']