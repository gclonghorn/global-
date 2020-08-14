from rest_framework import serializers
from users.models import User
from.models import Document

#用于创建文集
class DocCreateSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Document
        fields = ('id', 'name', 'create_user','content','parent_doc','role','type', 'modify_time', 'create_time','last_modify_user')


#用于编辑文集(作者不能被修改，只是改标题内容，id,type,role,status前端不传参,)
class DocUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'content',)


#用于展示文集列表
class DocListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id','name', 'create_user','last_modify_user')

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
    class Meta:
        model = Document
        fields = ('id', 'name','create_user', 'create_time', 'last_modify_user', 'modify_time')