
from rest_framework import serializers

from documents.models import Document
from message.models import Message

from users.models import User

#用于消息的创建者接收者
class UserSeirializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'head')

#用于展示关联文档
class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name')

#用于消息展示
class MessageSerializer(serializers.ModelSerializer):
    user = UserSeirializer()
    origin_user = UserSeirializer()
    document = DocSerializer()
    class Meta:
        model = Message
        fields = ('id', 'user', 'origin_user', 'document', 'time', 'type', 'status')

#用于单个消息更新
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'status')

#用于全部消息更新
class AllUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user')