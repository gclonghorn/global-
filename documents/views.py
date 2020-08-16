from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status, mixins, viewsets, authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from recentDoc.models import Recent
from .serializers import *
from .models import Document
from recycleBin.models import *
from team.models import Team
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import datetime
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
    list:
    查看协作者
    """
    queryset = Document.objects.all()
    serializer_class = DocCreateSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    #创建文档权限：团队创建者，可写协作者
    # 创建文档权限：团队创建者，可写协作者
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 创建团队空间 登录即可创建。
        if "type" not in serializer.validated_data:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            if serializer.validated_data["type"] == 1:  # 必须加引号！！！！！
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            # 创建文件
            elif serializer.validated_data["type"] == 0:
                # 创建个人文档
                if "parent_doc" not in serializer.validated_data:  # parent _doc 空创建单个文件
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else:  # 创建团队文档
                    project = serializer.validated_data["parent_doc"].id
                    # 请求的用户是团队的创建者。老大
                    check_project = Document.objects.filter(id=project, create_user=request.user)
                    # 请求用户是团队的协作者
                    colla_project = Team.objects.filter(document_id=project, user=request.user)
                    # 是老大/协作者
                    if check_project.count() > 0 or colla_project.count() > 0:
                        self.perform_create(serializer)
                        headers = self.get_success_headers(serializer.data)
                        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                    else:  # 请求失败
                        return Response(status=status.HTTP_401_UNAUTHORIZED)

            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        if "create_by_model" in serializer.validated_data:  # 有模板
            # 修改新建文档的content
            content_temp = Document.objects.get(
                id=serializer.validated_data["create_by_model"].id).serializable_value('content')
            name_temp = Document.objects.get(
                id=serializer.validated_data["create_by_model"].id).serializable_value('name')
            serializer.validated_data["content"] = content_temp
            serializer.validated_data["name"] = name_temp
        serializer.validated_data["last_modify_user"]= serializer.validated_data["create_user"]#add
        instance = serializer.save()
        project = instance.parent_doc  # 父文档
        # 新建文档继承团队的协作关系
        parentteams = Team.objects.filter(document_id=project)  # 团队的协作关系集合
        # inheritors =parentteam.values_list('user', flat=True)
        for parentteam in parentteams:
            Team.objects.create(document=instance, user=parentteam.user)
        # 团队的创建者不在协作关系里。

    # 编辑文档
    # 更新文档权限：团队创建者，可写协作者
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.type == 1:
            if Document.objects.filter(id=instance.id, create_user=request.user).count() > 0:
                self.perform_update(serializer)
                if getattr(instance, '_prefetched_objects_cache', None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        elif instance.type == 0:
            # 判断文档的status 不是request里发送的status，而是数据库中已经保存过的这个文档的status
            if instance.status == 1:
                if instance.parent_doc_id == None:  # 从数据库里取，不依赖前端发送 个人文档
                    # 公开文档或作者
                    if instance.role == 0 or Document.objects.filter(id=instance.id,
                                                                     create_user=request.user).count() > 0:
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    # 更新的文档和用户的协作关系存在 用户就是个人文档的协作者
                    elif Team.objects.filter(document_id=instance.id, user=request.user).count() > 0 and \
                            (instance.role == 1 or instance.role == 2):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                else:  # 团队文档
                    # if 老大 or 文档创建者 or role=0
                    if instance.role == 0 or Document.objects.filter(id=instance.id,
                                                                     create_user=request.user).count() > 0 or Document.objects.filter(
                            id=instance.parent_doc_id, create_user=request.user):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    # if 协作者 and 团队可读写
                    elif Team.objects.filter(document_id=instance.id, user=request.user).count() > 0 and \
                            (instance.role == 1 or instance.role == 2):
                        self.perform_update(serializer)
                        if getattr(instance, '_prefetched_objects_cache', None):
                            instance._prefetched_objects_cache = {}
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)  # 没权限改团队文档
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)  # 有人在编辑
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.status = 0  # 编辑后是草稿状态需要发布按钮才能复原为1
        #instance.last_modify_user=self.request.user
        print(self.request.user)
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.type == 1:  # 删除团队
            if Document.objects.filter(create_user=request.user, id=instance.id).count() > 0:  # 是团队创作者
                children = Document.objects.filter(parent_doc=instance.id)
                flag = True
                for child in children:
                    if child.status == 0: flag = False  # 有子文档是编辑状态，团队不能删除
                if flag:
                    self.perform_destroy(instance)
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)  # 有子文档是编辑状态，团队不能删除
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)  # 非创作者不能删除
        elif instance.type == 0:
            if instance.parent_doc == None:  # 删除个人文档
                # if  创建者
                if Document.objects.filter(create_user=request.user, id=instance.id).count() > 0:
                    self.perform_destroy(instance)
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:  # 删除团队文档
                # if 老大/文档创建者
                if Document.objects.filter(create_user=request.user,
                                           id=instance.id).count() > 0 or Document.objects.filter(
                        id=instance.parent_doc_id, create_user=request.user):
                    self.perform_destroy(instance)
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)  # 没权限删团队文档
        else:  # 文件类型出错
            return Response(status.HTTP_401_UNAUTHORIZED)

    def perform_destroy(self, instance):
        # 自己状态改2
        instance.status = 2
        # 子文档状态改2
        children = Document.objects.filter(parent_doc=instance.id)
        for child in children:
            child.status = 2
            child.modify_time = datetime.datetime.now()
            child.save()
            Recent.objects.filter(user=self.request.user, document=instance).delete()
            RecycleBin.objects.create(document=child, user=self.request.user)
        instance.modify_time = datetime.datetime.now()
        instance.save()
        # 避免重复添加删除记录
        RecycleBin.objects.filter(user=self.request.user, document=instance).delete()
        RecycleBin.objects.create(document=instance, user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return DocCreateSerializer
        elif self.action == 'update':
            return DocUpdateSerializer
        elif self.action == 'retrieve':
            return DocRetrieveSerializer
        return DocCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        #如果查看的是团队
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.type == 1 and instance.status!=2:
            # 请求的用户是团队的老大
            check_project = Document.objects.filter(create_user=request.user, id=instance.id)
            # 请求用户是团队的协作者
            colla_project = Team.objects.filter(document_id=instance.id, user=request.user)
            # 是老大/协作者
            if check_project.count() > 0 or colla_project.count() > 0:
                return Response(serializer.data)
            # 请求失败
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        #如果查看的是文档
        elif instance.type == 0 and status!=2:
            #如果是个人文档
            if instance.parent_doc == None:
                #请求者是文档创建者或者协作者可看
                check_author = Document.objects.filter(create_user=request.user, id=instance.id)
                colla_author = Team.objects.filter(document_id=instance.id, user=request.user)
                if check_author.count() > 0 or colla_author.count() > 0:
                    Recent.objects.filter(user=request.user, document=instance).delete()
                    Recent.objects.create(user=request.user, document=instance)
                    return Response(serializer.data)
                #文档权限是0，2
                elif instance.role == 0 or instance.role == 2:
                    Recent.objects.filter(user=request.user, document=instance).delete()
                    Recent.objects.create(user=request.user, document=instance)
                    return Response(serializer.data)
                #请求失败
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

            #如果是团队文档
            else:
                #请求者是老大、协作者可看
                # 请求的用户是老大
                project = instance.parent_doc
                check_project = Document.objects.filter(id=project.id, create_user=request.user)
                # 请求用户是老大、团队的协作者
                colla_project = Team.objects.filter(document_id=instance.id, user=request.user)
                if check_project.count() > 0 or colla_project.count() > 0:
                    Recent.objects.filter(user=request.user, document=instance).delete()
                    Recent.objects.create(user=request.user, document=instance)
                    return Response(serializer.data)
                #文档权限是0，2
                elif instance.role == 0 or instance.role == 2:
                    Recent.objects.filter(user=request.user, document=instance).delete()
                    Recent.objects.create(user=request.user, document=instance)
                    return Response(serializer.data)
                #请求失败
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class DocRoleEditViewset(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocRoleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # 请求修改个人文档权限
        if instance.type == 0 and instance.parent_doc == None:
            # 请求的用户是文档的创建者
            check_author = Document.objects.filter(create_user=request.user, id=instance.id)
            if check_author.count() > 0:
                if instance.role == 0 or instance.role == 1 or instance.role == 2 or instance.role == 3:
                    self.perform_update(serializer)
                    if getattr(instance, '_prefetched_objects_cache', None):
                        # If 'prefetch_related' has been applied to a queryset, we need to
                        # forcibly invalidate the prefetch cache on the instance.
                        instance._prefetched_objects_cache = {}
                    return Response(serializer.data)

                else:  # role值非法
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:  # 没有权限
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        # 请求修改团队文档权限
        elif instance.type == 0 and instance.parent_doc != None:
            project = instance.parent_doc
            # 请求的用户是老大
            check_project = Document.objects.filter(id=project.id, create_user=request.user)
            # 请求用户是文档创建者
            colla_project = Document.objects.filter(id=instance.id, create_user=request.user)
            # 是老大/创建者
            if check_project.count() > 0 or colla_project.count() > 0:
                if instance.role == 0 or instance.role == 1 or instance.role == 2 or instance.role == 3:
                    self.perform_update(serializer)
                    if getattr(instance, '_prefetched_objects_cache', None):
                        # If 'prefetch_related' has been applied to a queryset, we need to
                        # forcibly invalidate the prefetch cache on the instance.
                        instance._prefetched_objects_cache = {}
                    return Response(serializer.data)
                else:  # role值非法
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:  # 没有权限
                return Response(status=status.HTTP_400_BAD_REQUEST)
        # 非文档类型
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DocStatusEditViewset(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocStatusSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        #是文档，不分个人文档还是团队文档，都可以修改状态
        if instance.type == 0:
            if instance.status == 0 or instance.status == 1 or instance.status == 2:
                self.perform_update(serializer)
                Document.objects.filter(id=instance.id).update(last_modify_user=request.user)
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
            #状态码非法
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        #非文档类型
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CoworkerViewset(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = CoworkerSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def retrieve(self, request, *args, **kwargs):
        # 得到文档实例，即针对哪个文档看协作者
        instance = self.get_object()
        # 查找Team里该文档的协作记录
        cos = Team.objects.filter(document_id=instance.id)
        aws = []
        ids = []
        person = User.objects.get(id=instance.create_user.id)
        d = {'id':person.id, 'username':person.username, 'head':str(person.head)}
        aws.append(d)
        ids.append(person.id)
        for co in cos:
            person = User.objects.get(id=co.user_id)
            if person.id not in ids:
                d = {'id': person.id, 'username': person.username, 'head':str(person.head)}
                aws.append(d)
                ids.append(person.id)
        return JsonResponse(aws, safe=False)


class MyTeamViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DocSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def list(self, request, *args, **kwargs):
        #找出所有团队
        teams = Team.objects.filter(user_id=request.user)
        ids = []
        for team in teams:
            ids.append(team.document_id)
        #找出我的团队
        self.queryset = Document.objects.filter(Q(id__in=ids)|Q(create_user=request.user), Q(type=1),~Q(status=2))

        queryset = self.filter_queryset(self.queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MyDocViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DocSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def list(self, request, *args, **kwargs):
        #找出所有team
        teams = Team.objects.filter(user_id=request.user)
        ids = []
        for team in teams:
            ids.append(team.document_id)
        # 找出我的文档
        self.queryset = Document.objects.filter(Q(id__in=ids)|Q(create_user=request.user), Q(type=0),~Q(status=2))

        queryset = self.filter_queryset(self.queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ChildDocViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DocSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.type == 1:
            childs = Document.objects.filter(parent_doc=instance)
            aws = []
            for child in childs:
                create = User.objects.get(id=child.create_user_id)
                if User.objects.filter(id = child.last_modify_user_id).count() > 0:
                    last = User.objects.get(id=child.last_modify_user_id)
                    d = {'id': child.id, 'name': child.name, 'create_user': create.id,
                         'create_user_username': create.username, 'create_user_head': str(create.head),
                         'content': child.content,
                         'parent_doc': child.parent_doc_id, 'role': child.role, 'type': child.type,
                         'modify_time': child.modify_time, 'create_time': child.create_time,
                         'last_modify_user': child.last_modify_user_id, 'last_modify_user_username': last.username,
                         'last_modify_user_head': str(last.head)}
                else:
                    d = {'id': child.id, 'name': child.name, 'create_user': create.id,
                         'create_user_username': create.username, 'create_user_head': str(create.head),
                         'content': child.content,
                         'parent_doc': child.parent_doc_id, 'role': child.role, 'type': child.type,
                         'modify_time': child.modify_time, 'create_time': child.create_time,
                         'last_modify_user': None, 'last_modify_user_username': None,
                         'last_modify_user_head': None}
                aws.append(d)
            return JsonResponse(aws, safe=False)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

#模板列表
class TemplatesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TemplateSerializer
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend)
    search_fields = ('name',)
    def get_queryset(self):
        self.queryset=Document.objects.filter(type=2)
        return self.queryset




