from django.db import models
from documents.models import *
from users.models import *
# Create your models here.
class Recent(models.Model):
    document = models.ForeignKey(Document,on_delete=models.CASCADE,verbose_name='文集')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    read_time = models.DateTimeField(auto_now_add=True,verbose_name='修改时间')

    def __str__(self):
        return self.document

    class Meta:
        verbose_name = '最近浏览'