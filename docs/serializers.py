from rest_framework import serializers
from.models import Doc

#用于创建文档
class DocEditSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Doc
        fields = ('id','name', 'content','parent_doc','top_doc','create_user','status')
#用于修改文档（作者不能被修改）
class DocUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = ('id','name', 'content','parent_doc','top_doc','status')
#用于展示下一级文档的信息
class ChildDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = ('id','name','parent_doc','top_doc','status')

#用于查看文档
class DocDetailSerializer(serializers.ModelSerializer):
    child_docs=ChildDocSerializer(many=True)
    class Meta:
        model = Doc
        fields = ('id','name', 'content','parent_doc','top_doc','create_user','status','child_docs')

#用于回收站列表
class RecycleListSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Doc
        fields = ('id','name', 'modify_time','create_user','status')