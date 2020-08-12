from django.db import models
from users.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="文集名称",max_length=50)
    create_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文集创建者")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="文集创建时间")
    modify_time = models.DateTimeField(auto_now=True,verbose_name="文集更新时间")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文集'
