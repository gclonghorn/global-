from rest_framework import viewsets
from rest_framework import mixins
from.models import Collaborator
from .serializers import EditColSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class EditColViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    create:增加文集协作
    destroy:删除文集协作
    '''
    queryset=Collaborator.objects.all()
    serializer_class = EditColSerializer

