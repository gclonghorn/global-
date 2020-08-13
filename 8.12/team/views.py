from django.db.models import Q
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status, authentication
from rest_framework import mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Team, User
from documents.models import Document
from .serializers import EditTeamSerializer


def get(instance):
    # 查找Team里该文档的协作记录
    cos = Team.objects.filter(document_id=instance.id)
    aws = []
    ids = []
    person = User.objects.get(id=instance.create_user.id)
    d = {'id': person.id, 'username': person.username, 'head': str(person.head)}
    aws.append(d)
    ids.append(person.id)
    for co in cos:
        person = User.objects.get(id=co.user_id)
        if person.id not in ids:
            d = {'id': person.id, 'username': person.username, 'head': str(person.head)}
            aws.append(d)
            ids.append(person.id)
    return aws

# Create your views here.
class EditTeamViewset(mixins.CreateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    '''
    create:增加文集协作
    destroy:删除文集协作
    '''
    queryset=Team.objects.all()
    serializer_class = EditTeamSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    #如果之前已经加入协作报400的错
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.validated_data['document']
        #如果是为团队添加协作关系
        if doc.type == 1:
            # 请求的用户是团队的老大
            check_project = Document.objects.filter(create_user=request.user, id=doc.id)
            # 请求用户是团队的协作者
            colla_project = Team.objects.filter(document_id=doc.id, user=request.user)
            if check_project.count() > 0 or colla_project.count() > 0:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                coworker = get(doc)
                return JsonResponse(coworker, safe=False)
                # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:  # 请求失败
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        #如果是为文档添加协作关系
        elif doc.type == 0:
            # 为个人文档添加协作关系
            if doc.parent_doc == None:
                # 请求者是文档创建者或者协作者
                check_author = Document.objects.filter(create_user=request.user, id=doc.id)
                colla_author = Team.objects.filter(document_id=doc.id, user=request.user)
                if check_author.count() > 0 or colla_author.count() > 0:
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                    # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            #为团队文档添加协作关系
            else:
                project = doc.parent_doc
                # 请求的用户是团队的老大
                check_project = Document.objects.filter(id=project.id, create_user=request.user)
                # 请求用户是团队的协作者
                colla_project = Team.objects.filter(document_id=project, user=request.user)
                if check_project.count() > 0 or colla_project.count() > 0:
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                    # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else:  # 请求失败
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        instance = serializer.save()
        doc = Document.objects.get(id=instance.document_id)
        if doc.type == 1:
            child_docs_list = Document.objects.filter(parent_doc=instance.document_id)  # 项目下属文档
            for child_doc in child_docs_list:
                Team.objects.create(document=child_doc, user=instance.user)




