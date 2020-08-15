from django.db import models
from documents.models import Document
from users.models import User


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, related_name='receive', on_delete=models.CASCADE,verbose_name="消息接收者")
    origin_user = models.ForeignKey(User, related_name='send', on_delete=models.CASCADE, verbose_name="消息发送人")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='消息关联的文档/团队')
    time = models.DateTimeField(auto_now_add=True, verbose_name="消息发送时间")
    #1:团队邀请信息（给被邀请人发）
    #2:加入团队结果（给邀请人+老大发）
    #3:退出团队结果（给老大发）
    #4:被踢出团队提醒（给被踢的人发）
    #5:被加入协作者提醒（给被邀请人发）
    #6:文档被评论（给被评论的文档的创建者+协作者发）
    #7:评论被回复（给被回复的评论人发）
    #8:退出文档协作者结果（给创建者发）
    #9：被踢出文档协作者提醒（给被踢的人发）
    type = models.IntegerField(default=0,verbose_name="消息类型")
    #消息状态 0未读， 1已读
    status = models.IntegerField(default=0, verbose_name='文档状态')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '消息'
