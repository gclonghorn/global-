from rest_framework import serializers
from.models import Project

#用于增删改文集
class ProjectEditSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = ('id','name', 'create_user',)

#用于展示文集列表
class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','name', 'create_user','project_docs')