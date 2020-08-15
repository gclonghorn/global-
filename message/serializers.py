
from rest_framework import serializers
from message.models import Message


#用于消息展示
class MessageSerializer(serializers.ModelSerializer):
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