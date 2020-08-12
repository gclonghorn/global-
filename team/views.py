from rest_framework import viewsets
from rest_framework import mixins
from.models import Team
from documents.models import Document
from .serializers import EditTeamSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class EditTeamViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    create:增加文集协作
    destroy:删除文集协作
    '''
    queryset=Team.objects.all()
    serializer_class = EditTeamSerializer

    def perform_create(self, serializer):
        instance=serializer.save()
        child_docs_list = Document.objects.filter(parent_doc=instance.document_id)  # 项目下属文档
        while (child_docs_list):
            child_docs_ids = child_docs_list.values_list('id', flat=True)  # 下级文档id列表
            for child_doc in child_docs_list:
                Team.objects.create(document=child_doc,user=instance.user)
            child_docs_list = Document.objects.filter(parent_doc__in=list(child_docs_ids))  # 更新下级文档列表
