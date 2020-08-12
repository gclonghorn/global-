from django.shortcuts import render
from rest_framework import status, mixins, viewsets, authentication, permissions,filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Doc
import datetime
from.filters import DocsFilter
from django_filters.rest_framework import  DjangoFilterBackend
from projects.models import *
from collaborators.models import *
from rest_framework.response import Response
# Create your views here.
#编辑文档
class DocEditViewset(mixins.RetrieveModelMixin,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """"
    create:
    创建文档
    destroy:
    删除文档
    update:
    修改文档
    retrieve:
    查看文档
    """
    queryset = Doc.objects.all()
    serializer_class = DocEditSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    #创建文档权限：团队创建者，可写协作者
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project =  request.data['top_doc']
        # 请求的用户是团队的创建者
        check_project = Project.objects.filter(id=project, create_user=request.user)
        # 请求用户是团队的可写协作者
        colla_project = Collaborator.objects.filter(project_id=project, user=request.user,role=0)
        # 请求创建文档
        if check_project.count() > 0 or colla_project.count() > 0:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED,headers=headers)

    # 更新文档权限：团队创建者，可写协作者
    def update(self, request, *args, **kwargs):
        '''
        if ("top_doc" in request.data) :
            pass
        else
            return JsonResponse({'status':False,'data':'无权操作此文集'}'''
        project=request.POST.get('top_doc','')
        #project = request.data['top_doc']
        # 请求的用户是团队的创建者
        check_project = Project.objects.filter(id=project, create_user=request.user)
        # 请求用户是团队的可写协作者
        colla_project = Collaborator.objects.filter(project_id=project, user=request.user, role=0)
        if check_project.count() > 0 or colla_project.count() > 0:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    #删除文档权限：文档创建者/团队创建者
    '''
    def destroy(self, request, *args, **kwargs):
        project = request.data['top_doc']
        # 请求的用户是团队的创建者
        check_project = Project.objects.filter(id=project, create_user=request.user)
        # 请求用户是文档的创建者
        if check_project.count() > 0 or request.user=request:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)'''
    #软删除 将下属文档一起软删除
    def perform_destroy(self, instance):
        instance.status=3
        instance.modify_time= datetime.datetime.now()
        instance.save()

        child_docs_list =  Doc.objects.filter(parent_doc=instance.id)  #项目下属文档
        while(child_docs_list):
            child_docs_ids=child_docs_list.values_list('id',flat=True) #下级文档id列表
            child_docs_list.update(status=3, modify_time=datetime.datetime.now())  # 修改下级文档的状态为删除
            child_docs_list=  Doc.objects.filter(parent_doc__in=list(child_docs_ids))  #更新下级文档列表

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DocDetailSerializer
        elif self.action=='create':
            return DocEditSerializer
        return DocUpdateSerializer


#回收站
class DocRecycleViewset(mixins.RetrieveModelMixin,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    '''
    list:
    查看回收站列表
    update:
    还原文档
    destroy:
    彻底删除文档
    '''
    #获取状态为删除 3 的文档，且创建人是登录用户
    queryset = Doc.objects.all()
    serializer_class = RecycleListSerializer
    def get_queryset(self):
        self.queryset= Doc.objects.filter(status=3,create_user=self.request.user).order_by('-modify_time')
        return self.queryset
    '''
    def perform_update(self, serializer):
        instance=serializer.save()
        instance.status=1    #还原为发布状态
        instance.save()
    '''
#查看文集下的一级文档
class DocListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    文档列表
    """

    queryset = Doc.objects.all()
    serializer_class = ChildDocSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend)
    filter_class = DocsFilter
    search_fields = ('name', 'content')
    ordering_fields = ('create_time', 'modify_time')