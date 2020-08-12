from django.db import models
from projects.models import Project
from users.models import User
# Create your models here.
class Collaborator(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='文集')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    #0可编辑，1仅查看
    role =models.IntegerField(default=1,verbose_name="权限等级")
    create_time = models.DateTimeField(auto_now=True,verbose_name='添加时间')
    modify_time = models.DateTimeField(auto_now_add=True,verbose_name='修改时间')

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = '文集协作'