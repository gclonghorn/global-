from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from projects.models import Project
from.serializers import ProjectEditSerializer,ProjectListSerializer
from docs.serializers import ChildDocSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from collaborators.models import Collaborator

# Create your views here.
#编辑文集
class ProjectEditViewset(mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """"
    list:
    我创建的文集列表
    create:
    创建文集
    destroy:
    删除文集
    update:
    修改文集名称
    retireve:
    展示文集信息不展示文集下的文件
    """
    queryset = Project.objects.all()
    serializer_class = ProjectEditSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    '''
    def get_queryset(self):
        self.queryset= Project.objects.filter(create_user=self.request.user)
        return self.queryset
    '''

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        elif self.action == 'create':
            self.permission_classes = (IsAuthenticated,)  #最后的，必须加上
        elif self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,)
        elif self.action =='list':
            self.permission_classes = (IsAuthenticated,)
        return [permission() for permission in self.permission_classes]

    def perform_destroy(self, instance):
        project_docs_list = instance.project_docs  #项目下属文档
        project_docs_list.remove()
        instance.delete()
    def get_serializer_class(self):
        if self.action =='list':
            return ProjectListSerializer
        return ProjectEditSerializer

#左侧栏文集列表，含我创建的，我加入的

class ProjectListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    文集列表
    """
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        col_list=Collaborator.objects.filter(user=self.request.user)
        col_list_pros=col_list.values_list('project_id',flat=True)

        self.queryset = Project.objects.filter(Q(create_user=self.request.user)
                                               |Q(id__in=list(col_list_pros)))
        return self.queryset


