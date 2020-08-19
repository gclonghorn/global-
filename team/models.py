from django.db import models
from documents.models import *
from users.models import *
# Create your models here.
class Team(models.Model):
    document = models.ForeignKey(Document,on_delete=models.CASCADE,verbose_name='文集')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户',null=True,blank=True)
    create_time = models.DateTimeField(auto_now=True,verbose_name='添加时间')
    modify_time = models.DateTimeField(auto_now_add=True,verbose_name='修改时间')
    role=models.IntegerField(default=0, verbose_name='0协作者1管理者2上级协作者')

    def __str__(self):
        return self.document

    class Meta:
        verbose_name = '文集协作'