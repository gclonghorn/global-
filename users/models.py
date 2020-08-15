from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
    用户信息
    """
    mobile = models.CharField(blank=True,max_length=11,verbose_name='电话')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    head = models.ImageField(upload_to='upload', null=True, blank=True, verbose_name="头像", help_text="头像")
    collect_num = models.IntegerField(default=0, verbose_name="已收藏文档数", help_text="已收藏文档数")

    class Meta:
        verbose_name = "用户信息"  #在admin站点显示名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code