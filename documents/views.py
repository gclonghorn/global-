from django.shortcuts import render
from rest_framework import status, mixins, viewsets, authentication, permissions,filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Document
from django.http.response import JsonResponse
import datetime
#from.filters import DocsFilter
from django_filters.rest_framework import  DjangoFilterBackend
from projects.models import *
from team.models import Team
from rest_framework.response import Response
import json
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
    queryset = Document.objects.all()
    serializer_class = DocCreateSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    #创建文档权限：团队创建者，可写协作者
    def create(self, request, *args, **kwargs):
        # 创建团队空间 登录即可创建。
        if request.data['type'] =='1':       #必须加引号！！！！！
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        #创建文件
        elif request.data['type'] == '0':
            #创建个人文档
            if request.data['parent_doc'] == '': #parent _doc 空创建单个文件
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:  #创建团队文档
                project = request.data['parent_doc']
                # 请求的用户是团队的创建者。老大
                check_project = Document.objects.filter(id=project, create_user=request.user)
                # 请求用户是团队的协作者
                colla_project = Team.objects.filter(document_id=project, user=request.user)
                # 是老大/协作者
                if check_project.count() > 0 or colla_project.count() > 0:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else: #请求失败
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        instance=serializer.save()
        project=instance.parent_doc #父文档
        # 新建文档继承父空间的协作关系
        parentteams= Team.objects.filter(document_id=project)#父空间的协作关系集合
        #inheritors =parentteam.values_list('user', flat=True)
        for parentteam in parentteams:
            Team.objects.create(document=instance, user=parentteam.user,role=parentteam.role)
    #编辑文档
    # 更新文档权限：团队创建者，可写协作者
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.type== 1:
            if Document.objects.filter(id=instance.id,create_user=request.user).count()>0:
                self.perform_update(serializer)
                if getattr(instance, '_prefetched_objects_cache', None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
            else :return Response(status=status.HTTP_401_UNAUTHORIZED)
        elif instance.type == 0:
            #判断文档的status 不是request里发送的status，而是数据库中已经保存过的这个文档的status
            if instance.status==1:
                if instance.parent_doc_id == None: #从数据库里取，不依赖前端发送 个人文档
                    if instance.role ==0 or request.user==instance.create_user:
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    #更新的文档和用户的协作关系存在 用户就是个人文档的协作者
                    elif Team.objects.filter(document_id=instance.id,user=request.user).count()>0 and \
                            (instance.role==1 or instance.role==2):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    else:return Response(status=status.HTTP_204_NO_CONTENT)
                else:#团队文档
                    #if 老大 or 文档创建者 or role=0
                    if instance.role == 0 or request.user == instance.create_user or Document.objects.filter(id=instance.parent_doc_id,create_user=request.user):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    elif Team.objects.filter(document_id=instance.id,user=request.user).count()>0 and \
                            (instance.role==1 or instance.role==2):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    else:return Response(status=status.HTTP_401_UNAUTHORIZED)#没权限改团队文档
                    return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            else:return Response(status=status.HTTP_401_UNAUTHORIZED)#有人在编辑
        else :return Response(status=status.HTTP_401_UNAUTHORIZED)

    def perform_update(self, serializer):
        instance=serializer.save()
        instance.status=0 #编辑后是草稿状态需要发布按钮才能复原为1
        instance.save()

    def get_serializer_class(self):
        if self.action=='create':
            return DocCreateSerializer
        elif self.action=='update':
            return DocUpdateSerializer
        return DocCreateSerializer
