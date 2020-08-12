from django.db import models
from users.models import User
from projects.models import Project
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Document(models.Model):
    name = models.CharField(verbose_name="文档标题",max_length=50)
    content = RichTextUploadingField(verbose_name="文档内容",null=True,blank=True)
    parent_doc = models.ForeignKey('self',related_name='child_docs',on_delete=models.CASCADE,verbose_name="上级文件夹",null=True,blank=True)
    #top_doc = models.ForeignKey('self',related_name='project_docs',on_delete=models.CASCADE,verbose_name="团队空间顶级文件夹",null=True,blank=True)
    create_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文档创建者")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="文档创建时间")
    modify_time = models.DateTimeField(auto_now=True,verbose_name="文档修改时间")
    # 0是文件 1是团队空间（文件夹）
    type =models.IntegerField(default=0,verbose_name="是否文件夹")
    # 0是草稿状态 1是发布状态 2是软删除状态
    status = models.IntegerField(default=1, verbose_name='文档状态')
    #权限 0公开 1私密 2 3
    role = models.IntegerField(default=1, verbose_name='文档权限')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文档'