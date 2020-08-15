from rest_framework import serializers

from users.models import User
from.models import *
from documents.models import Document
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

#用于展示回收站
class RecycleDocSerializer(serializers.ModelSerializer):
    document = DocSerializer()
    class Meta:
        model = RecycleBin
        fields = ('document','delete_time')
#用于编辑回收站文档
class RecycleEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

