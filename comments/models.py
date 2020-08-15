from django.db import models
from users.models import *
from documents.models import *
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Comment (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='comments',  verbose_name="作者")
    document=models.ForeignKey(Document, on_delete=models.CASCADE, default=1, related_name='comments', verbose_name="文章", help_text="被评论文章")
    body = RichTextUploadingField(verbose_name="评论内容", help_text="评论内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="文档创建时间")
    reply_comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True,help_text="父级评论")
    #related_name 便于主表查子表即评论有哪些回复 .reply_comment说明这条评论属于哪个

    class Meta:
        ordering=('-create_time',)

    def _unicode_(self):
        return self.body
class Collect (models.Model):
    """
    用户收藏
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,related_name='collects', verbose_name="收藏者",help_text="收藏者")
    document=models.ForeignKey(Document, on_delete=models.CASCADE, default=1,related_name='collects', verbose_name="文章",help_text="被收藏文章")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="收藏创建时间")

    class Meta:
        ordering=('-create_time',)
        unique_together = ("author", "document")  #一个用户对一个文章只能收藏一次

    def _unicode_(self):
        return self.author.username