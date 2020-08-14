from rest_framework import serializers

from users.models import User
from.models import Recent
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

#用于展示最近浏览
class RecentDocSerializer(serializers.ModelSerializer):
    document = DocSerializer()
    class Meta:
        model = Recent
        fields = ('document','read_time')

