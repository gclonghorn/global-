from django.db import models
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Document(models.Model):
    name = models.CharField(verbose_name="文档标题",max_length=50)
    content = RichTextUploadingField(verbose_name="文档内容",null=True,blank=True)
    parent_doc = models.ForeignKey('self',related_name='child_docs',on_delete=models.CASCADE,verbose_name="上级文件夹",null=True,blank=True)
    create_user = models.ForeignKey(User, related_name='create', on_delete=models.CASCADE,verbose_name="文档创建者")
    last_modify_user = models.ForeignKey(User,related_name='modify', on_delete=models.CASCADE, verbose_name="最后修改者", null=True)
    editor=models.ForeignKey(User, related_name='edit', on_delete=models.CASCADE,verbose_name="当前编辑者",null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="文档创建时间")
    modify_time = models.DateTimeField(auto_now=True,verbose_name="文档修改时间")
    # 0是文件 1是团队空间（文件夹）
    type =models.IntegerField(default=0,verbose_name="是否文件夹")
    # 0是草稿状态 1是发布状态 2是软删除状态
    status = models.IntegerField(default=1, verbose_name='文档状态')
    # 权限
    # 0完全公开：所有人可读可写
    # 1团队公开：团队成员可读可写，团队外不可读写
    # 2团队读写：团队成员可读可写，团队外可读
    # 3团队只读：团队成员可读，创建者可写，团队外不可读写
    role = models.IntegerField(default=0, verbose_name='0完全公开1团队公开2团队读写3团队只读')
    #模板
    create_by_model=models.ForeignKey('self', on_delete=models.CASCADE,  related_name='model', verbose_name="文档模板", null=True,blank=True,help_text="模板")
    thumbnail=models.ImageField(upload_to='upload', null=True, blank=True, verbose_name="缩略图", help_text="缩略图")
    #now_editor= models.ForeignKey(User,related_name='edit', on_delete=models.CASCADE, verbose_name="当前编辑者", null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文档'
