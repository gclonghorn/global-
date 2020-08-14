from django.db.models import Q
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status, authentication
from rest_framework import mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from message.models import Message
from .models import Team, User
from documents.models import Document
from .serializers import EditTeamSerializer, DeleteMemberSerializer

#获取协作者+创建者
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



#增加团队/文档协作
class AddMemberViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:增加文集协作
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
        person = serializer.validated_data['user']
        #如果是为团队添加协作关系
        if doc.type == 1:
            # 请求的用户是团队的老大
            check_project = Document.objects.filter(create_user=request.user, id=doc.id)
            # 请求用户是团队的协作者
            colla_project = Team.objects.filter(document_id=doc.id, user=request.user)
            if check_project.count() > 0 or colla_project.count() > 0:
                #给被邀请人发送type1消息
                Message.objects.create(user=person, document=doc, origin_user=request.user, type=1)
                coworker = get(doc)
                return JsonResponse(coworker, safe=False)
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
                    # 给被加入协作者的人发type5消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=5)
                    #获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
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
                    # 给被加入协作者的人发type5消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=5)
                    #获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
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



class DeleteMemberViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:删除文集协作
    '''
    queryset=Team.objects.all()
    serializer_class = DeleteMemberSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    #如果之前已经加入协作报400的错
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.validated_data['document']
        person = serializer.validated_data['user']
        #如果没有该协作记录，返回401
        if Team.objects.filter(document=doc, user=person).count() == 0:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        #获得Team的instance
        instance = Team.objects.get(document=doc, user=person)
        #如果是为团队删除协作关系
        if doc.type == 1:
            # 请求的用户是团队的老大，则给被踢的人发type4消息
            check_project = Document.objects.filter(create_user=request.user, id=doc.id)
            # 请求用户是要删除的人，则给老大发type3消息
            myself = Team.objects.filter(Q(user=request.user), Q(user=person))
            #请求的用户是团队的老大
            if check_project.count() > 0:
                self.perform_destroy(instance)
                #给被踢的人发type4消息
                Message.objects.create(user=person, document=doc, origin_user=request.user, type=4)
                #获取协作者列表
                coworker = get(doc)
                return JsonResponse(coworker, safe=False)
            # 请求用户是要删除的人
            elif myself.count() > 0:
                self.perform_destroy(instance)
                #给老大发type3消息
                Message.objects.create(user=doc.create_user, document=doc, origin_user=request.user, type=3)
                # 获取协作者列表
                coworker = get(doc)
                return JsonResponse(coworker, safe=False)
            else:  # 请求失败
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        #如果是为文档删除协作关系
        elif doc.type == 0:
            # 为个人文档删除协作关系
            if doc.parent_doc == None:
                # 请求者是文档创建者，则给被踢的人发type9消息
                check_author = Document.objects.filter(create_user=request.user, id=doc.id)
                #请求者是删除本人，则给创建者发type8消息
                myself = Team.objects.filter(Q(user=request.user),Q(user=person))
                #请求的人是创建者
                if check_author.count() > 0:
                    self.perform_destroy(instance)
                    # 给被踢的人发type9消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=9)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                #请求的人是删除者本人
                elif myself.count() > 0:
                    self.perform_destroy(instance)
                    # 给创建者发type8消息
                    Message.objects.create(user=doc.create_user, document=doc, origin_user=request.user, type=8)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            #为团队文档删除协作关系
            else:
                project = doc.parent_doc
                # 请求的用户是团队的老大，则给被踢的人发type9消息
                check_project = Document.objects.filter(id=project.id, create_user=request.user)
                # 请求用户是文档创建者，则给被踢的人发type9消息
                colla_project = Document.objects.filter(id=doc.id, create_user=request.user)
                #请求删除用户是自己，则给创建者和老大发type8消息
                myself = Team.objects.filter(Q(user=request.user), Q(user=person))
                #请求的用户是团队的老大或文档创建者
                if check_project.count() > 0 or colla_project.count() > 0:
                    self.perform_destroy(instance)
                    # 给被踢的人发type9消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=9)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                #请求删除用户是自己
                elif myself.count()>0:
                    self.perform_destroy(instance)
                    # 给创建者和老大发type8消息
                    Message.objects.create(user=doc.create_user, document=doc, origin_user=request.user, type=8)
                    Message.objects.create(user=project.create_user, document=doc, origin_user=request.user, type=8)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                else:  # 请求失败
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
        doc = Document.objects.get(id=instance.document_id)
        if doc.type == 1:
            child_docs_list = Document.objects.filter(parent_doc=instance.document_id)  # 项目下属文档
            for child_doc in child_docs_list:
                Team.objects.filter(document=child_doc, user=instance.user).delete()


#接受邀请
class AcceptInvitationViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
        create:增加团队协作，给老大发type2消息
    '''
    queryset = Team.objects.all()
    serializer_class = EditTeamSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # 如果之前已经加入协作报400的错
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.validated_data['document']
        # 如果是为团队添加协作关系
        if doc.type == 1:
            self.perform_create(serializer)
            coworker = get(doc)
            return JsonResponse(coworker, safe=False)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        instance = serializer.save()
        doc = Document.objects.get(id=instance.document_id)
        if doc.type == 1:
            child_docs_list = Document.objects.filter(parent_doc=instance.document_id)  # 项目下属文档
            for child_doc in child_docs_list:
                Team.objects.create(document=child_doc, user=instance.user)

        #给老大发2消息
        leader = doc.create_user
        Message.objects.create(user=leader, origin_user=instance.user, document=doc, type=2)




