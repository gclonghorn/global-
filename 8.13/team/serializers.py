from rest_framework import serializers

from documents.models import Document
from users.models import User
from.models import Team
from rest_framework.validators import UniqueTogetherValidator

#用于增加修改文集协作
class EditTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('document','user')
        validators = [
            UniqueTogetherValidator(queryset=Team.objects.all(), fields=('document','user'), message='已加入协作')
        ]


#用于删除修改文集协作
class DeleteMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('document','user')

