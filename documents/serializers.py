from rest_framework import serializers
from.models import Document

#用于创建文集
class DocCreateSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Document
        fields = ('id','name', 'create_user','content','parent_doc','type')

#用于编辑文集(作者不能被修改，只是改标题内容，id,type,role,status前端不传参,)
class DocUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'content',)

#用于展示文集列表
class DocListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id','name', 'create_user','project_docs')