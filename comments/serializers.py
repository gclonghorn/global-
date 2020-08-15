from users.models import *
from .models import *
from documents.models import *
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
#用于评论者概要信息
class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')


#序列化父子评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    author=UserSrializer()
    class Meta:
       model = Comment
       fields = ('id','author','body','create_time')  #若添加删除功能fields需包含“id"字段


#用于增删评论
class CommentEditSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id','author','document','body','reply_comment',)  #若添加删除功能fields需包含“id"字段
#用于博文详情页展示评论详情
class CommentDetailSerializer(serializers.ModelSerializer):

    reply_comment = ReplyCommentSerializer()
    author = UserSrializer()
    replies=ReplyCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id','author','document','body','create_time','reply_comment','replies')#reply_comment:回复的哪个  replies:有哪些回复

#用于增删收藏
class LikeSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Collect
        fields = ('author','document','id')  #若添加删除功能fields需包含“id"字段
        validators = [
            UniqueTogetherValidator(queryset=Collect.objects.all(), fields=('author', 'document'), message='已经收藏')
        ]
#用于收藏列表展示文档详情
class DocSerializer(serializers.ModelSerializer):
    has_collect = serializers.SerializerMethodField()

    def get_has_collect(self, obj):
        collect = Collect.objects.filter(author=self.context['request'].user, document=obj).count()
        if collect > 0:
            data = 1
        else:
            data = 0
        return data
    class Meta:
        model = Document
        fields = ('create_user', 'name', 'id','modify_time','has_collect')  # 若添加删除功能fields需包含“id"字段

#用于收藏列表
class LikeDetailSerializer(serializers.ModelSerializer):
    document=DocSerializer()
    class Meta:
        model = Collect
        fields = ('author','document','id')  #若添加删除功能fields需包含“id"字段
