from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from docs.models import Doc
#from users.models import User
User=get_user_model()

# Create your models here.
class Comment (models.Model):
    dec=models.ForeignKey(Doc, on_delete=models.CASCADE, default=1, related_name='comments', verbose_name="文档", help_text="被评论文档")
    content = RichTextUploadingField(verbose_name="评论内容", help_text="评论内容")
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='comments',  verbose_name="创建评论者")
    create_time=models.DateTimeField(default=timezone.now, verbose_name="发表时间", help_text="发表时间")
    reply_comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True,help_text="父级评论")
    # related_name 便于主表查子表即评论有哪些回复 .reply_comment说明这条评论属于哪个

    class Meta:
        ordering = ['-create_time']

    def _unicode_(self):
        return self.content

class UserCol(models.Model):
    """
    用户收藏
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='collect', verbose_name="收藏者")
    dec = models.ForeignKey(Doc, on_delete=models.CASCADE, default=1, related_name='likes', verbose_name="文档",help_text="被收藏文档")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="收藏时间", help_text="用户收藏时间")

    class Meta:
        ordering = ['-create_time']
        unique_together = ("author", "dec")  # 一个用户对一个文档只能收藏一次

    def _unicode_(self):
        return self.author.username