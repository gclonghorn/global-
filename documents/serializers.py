from rest_framework import serializers
from users.models import User
from.models import Document
from comments.serializers import *
import json
#用于创建文集
class DocCreateSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Document
        fields = ('id','name', 'create_user','content','parent_doc'
                  ,'role','type','create_by_model')


#用于编辑文集(作者不能被修改，只是改标题内容，id,type,role,status前端不传参,)
class DocUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'content',)

#用于展示用户详细信息
#用于查看协作者
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "head")
# 用于查看文集
class DocRetrieveSerializer(serializers.ModelSerializer):
    create_user = UserSerializer()
    comments=CommentDetailSerializer(many=True)
    editor=UserSerializer()
    has_collect = serializers.SerializerMethodField()
    def get_has_collect(self, obj):
        collect = Collect.objects.filter(author=self.context['request'].user, document=obj).count()
        if collect >0:data =1
        else :data=0
        return data

    class Meta:
        model = Document
        fields = ('id','name', 'create_user','content','parent_doc','role',
                  'type', 'modify_time', 'create_time','last_modify_user','comments','has_collect','editor')
#用于展示文集列表
class DocListSerializer(serializers.ModelSerializer):
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
        fields = ('id','name', 'create_user','last_modify_user','has_collect')

#用于修改权限
class DocRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id','role')

#用于修改状态
class DocStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id','status')


#用于查看协作者
class CoworkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "head")

#用于文档创建者展示
class DocOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'head')

#用于控制文档/团队显示
class DocSerializer(serializers.ModelSerializer):
    create_user = DocOwnerSerializer()
    last_modify_user = DocOwnerSerializer()
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
        fields = ('id', 'name','create_user', 'create_time', 'last_modify_user', 'modify_time','has_collect')


#用于模板展示
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name','thumbnail')