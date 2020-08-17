from django.db import models
from documents.models import *
# Create your models here.
class RecycleBin (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="文档创建者")
    document= models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name="被删除文档")
    delete_time = models.DateTimeField(auto_now_add=True, verbose_name="文档删除时间")

    def __str__(self):
        return self.document
    class Meta:
        verbose_name = '删除记录'