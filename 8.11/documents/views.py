from rest_framework import status, mixins, viewsets, authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Document
from team.models import Team
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
    queryset = Document.objects.all()
    serializer_class = DocCreateSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    #创建文档权限：团队创建者，可写协作者
    def create(self, request, *args, **kwargs):
        # 创建团队空间 登录即可创建。
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        instance = serializer.save()
        project = instance.parent_doc  # 父文档
        # 新建文档继承父空间的协作关系
        parentteams = Team.objects.filter(document_id=project)  # 父空间的协作关系集合
        # inheritors =parentteam.values_list('user', flat=True)
        for parentteam in parentteams:
            Team.objects.create(document=instance, user=parentteam.user)

    def perform_create(self, serializer):
        instance=serializer.save()
        project=instance.parent_doc #父文档
        # 新建文档继承父空间的协作关系
        parentteams= Team.objects.filter(document_id=project)#父空间的协作关系集合
        #inheritors =parentteam.values_list('user', flat=True)
        for parentteam in parentteams:
            Team.objects.create(document=instance, user=parentteam.user,role=parentteam.role)


    def retrieve(self, request, *args, **kwargs):
        #如果查看的是团队
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.type == 1:
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
        elif instance.type == 0:
            #如果是个人文档
            if instance.parent_doc == None:
                #请求者是文档创建者或者协作者可看
                check_author = Document.objects.filter(create_user=request.user, id=instance.id)
                colla_author = Team.objects.filter(document_id=instance.id, user=request.user)
                if check_author.count() > 0 or colla_author.count() > 0:
                    return Response(serializer.data)
                #文档权限是0，2
                elif instance.role == 0 or instance.role == 2:
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
                    return Response(serializer.data)
                #文档权限是0，2
                elif instance.role == 0 or instance.role == 2:
                    return Response(serializer.data)
                #请求失败
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def update_role(self, request, *args, **kwargs):
        # 请求修改个人文档权限
        if request.data['type'] == '0' and request.data['parent_doc'] == '':
            # 请求的用户是文档的创建者
            check_author = Document.objects.filter(create_user=request.user)
            if check_author.count() > 0:
                if request.data['role'] == '0' or request.data['role'] == '1':
                    partial = kwargs.pop('partial', False)
                    instance = self.get_object()
                    serializer = self.get_serializer(instance, data=request.data, partial=partial)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                else:  # role值非法
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:  # 没有权限
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        # 请求修改团队文档权限
        elif request.data['type'] == '0' and request.data['parent_doc'] != '':
            project = request.data['parent_doc']
            # 请求的用户是团队的创建者。老大
            check_project = Document.objects.filter(id=project, create_user=request.user)
            # 请求用户是团队的协作者
            colla_project = Team.objects.filter(document_id=project, user=request.user)
            # 是老大/协作者
            if check_project.count() > 0 or colla_project.count() > 0:
                if request.data['role'] == '0' or request.data['role'] == '1':
                    partial = kwargs.pop('partial', False)
                    instance = self.get_object()
                    serializer = self.get_serializer(instance, data=request.data, partial=partial)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                else:  # role值非法
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:  # 没有权限
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        # 非文档类型
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def get_serializer_class(self):
        if self.action=='create':
            return DocCreateSerializer
        return DocCreateSerializer
