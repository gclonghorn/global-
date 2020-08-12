from rest_framework import serializers
from.models import Collaborator
from rest_framework.validators import UniqueTogetherValidator

#用于增加修改文集协作
class EditColSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaborator
        fields = ('project','user')
        validators = [
            UniqueTogetherValidator(queryset=Collaborator.objects.all(), fields=('project','user'), message='已加入协作')
        ]