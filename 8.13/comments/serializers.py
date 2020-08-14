from rest_framework import serializers
from.models import Comment,UserCol
from users.models import User
from rest_framework.validators import UniqueTogetherValidator

#用于评论者概要信息
class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')

#序列化被回复评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    create_user=UserSrializer()
    class Meta:
       model = Comment
       fields = ("id", "create_user")  #若添加删除功能fields需包含“id"字段

#序列化子评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    create_user=UserSrializer()
    class Meta:
       model = Comment
       fields = ('id','create_user','content','create_time')  #若添加删除功能fields需包含“id"字段


#用于增删评论
class CommentSerializer(serializers.ModelSerializer):
    create_user=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    #reply_comment = ReplyCommentSerializer()

    class Meta:
        model = Comment
        fields = ('id','create_user','content','reply_comment',)  #若添加删除功能fields需包含“id"字段

#用于文档展示评论详情
class CommentDetailSerializer(serializers.ModelSerializer):

    reply_comment = ReplyCommentSerializer()
    create_user = UserSrializer()
    replies=ReplyCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id','create_user','dec','content','create_time','reply_comment','replies')#reply_comment:回复的哪个  replies:有哪些回复

#用于文档详情页展示收藏者列表（暂无要求
# class LikeDetailSerializer(serializers.ModelSerializer):
#     create_user = UserSrializer()
#     class Meta:
#         model = Like
        # fields = ('create_user','id')

#用于增删收藏
class ColSerializer(serializers.ModelSerializer):
    create_user =serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserCol
        fields = ('create_user','dec','create_time','id')  #若添加删除功能fields需包含“id"字段
        validators = [
            UniqueTogetherValidator(queryset=UserCol.objects.all(), fields=('create_user', 'dec'), message='已经收藏')
        ]

class ColSerializerNew(serializers.ModelSerializer):
    create_user=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    create_user_id=serializers.SerializerMethodField(label='当前id')
    class Meta:
        model = UserCol
        fields = ('create_user','dec','create_time','id','create_user_id')  #若添加删除功能fields需包含“id"字段
        validators = [
            UniqueTogetherValidator(queryset=UserCol.objects.all(), fields=('create_user', 'dec'), message='已经收藏'                                                                                                  '')
        ]

    def get_create_user_id(self, obj):
        ID=obj.create_user.id
        return ID