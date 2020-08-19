from django.db.models import Q
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status, authentication
from rest_framework import mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from recycleBin.models import *
from message.models import Message
from .models import Team, User
from documents.models import Document
from .serializers import EditTeamSerializer, DeleteMemberSerializer

#获取协作者role=0+管理员role=1
def get(instance):
    # 查找Team里该文档的协作记录
    cos = Team.objects.filter(document_id=instance.id)
    aws = []
    for co in cos:
        person = User.objects.get(id=co.user_id)
        d = {'id': person.id, 'username': person.username, 'head': str(person.head),'role':co.role}
        aws.append(d)
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

    # 如果之前已经加入协作报400的错
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.validated_data['document']  #要添加协作关系的文档/团队
        person = serializer.validated_data['user'] #被添加人
        # 被添加者不存在
        if person == None:
            print(person)
            return Response(status=status.HTTP_204_NO_CONTENT)
        # 如果是为团队添加协作关系
        if doc.type == 1:
            # 请求用户是团队的协作者或团队的创建者
            colla_project = Team.objects.filter(document_id=doc.id, user=request.user)
            if colla_project.count() > 0:
                print(colla_project.count())
                '''
                # 如果被添加人是团队的创建者或协作者（这其中包含了自己），则返回400
                if Team.objects.filter(document_id=doc.id, user=person).count()>0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                这个判断多余了，因为team数据库设置了不能重复加，所以team已有的协作关系不能再加了
                '''
                #self.perform_create(serializer) 需要发送邀请，不能直接添加
                # 给被邀请人发送type1消息
                Message.objects.create(user=person, document=doc, origin_user=request.user, type=1)
                coworker = get(doc)
                return JsonResponse(coworker, safe=False)
            else:  # 没有权限给团队添加协作关系
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        # 如果是为文档添加协作关系
        elif doc.type == 0:
            # 为个人文档添加协作关系
            if doc.parent_doc == None:
                # 请求者是文档创建者或者协作者
                colla_project = Team.objects.filter(document_id=doc.id, user=request.user)
                if colla_project.count() > 0:
                    self.perform_create(serializer)
                    # 给被加入协作者的人发type5消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=5)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            # 为团队文档添加协作关系
            else:
                #添加人是团队创建者/团队协作者/文档创建者/文档协作者==team里有数据
                colla_project = Team.objects.filter(document_id=doc.id, user=request.user)
                if colla_project.count() > 0:
                    self.perform_create(serializer)
                    # 给被加入协作者的人发type5消息
                    Message.objects.create(user=person, document=doc, origin_user=request.user, type=5)
                    # 获取协作者列表
                    coworker = get(doc)
                    return JsonResponse(coworker, safe=False)
                else:  # 请求失败
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:#文档参数错误
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        instance = serializer.save()
        doc = Document.objects.get(id=instance.document_id)
        if doc.type == 1:
            child_docs_list = Document.objects.filter(parent_doc=instance.document_id)  # 这个人是项目下属文档的上级写作者
            for child_doc in child_docs_list:
                if Team.objects.filter(document=child_doc, user=instance.user).count() == 0:
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
        doc = serializer.validated_data['document'] #被解除协作关系的文档
        person = serializer.validated_data['user'] #被删除者
        #如果没有该协作记录，返回401
        if Team.objects.filter(document=doc, user=person).count() == 0:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        #获得Team的instance
        instance = Team.objects.get(document=doc, user=person)
        #如果是为团队删除协作关系
        if doc.type == 1:
            # 请求的用户是团队的老大，则给被踢的人发type4消息
            # 请求用户是要删除的人，且请求者是普通协作者，则给老大发type3消息
            myself = Team.objects.filter(Q(user=request.user), Q(user=person),role=0)
            #请求的用户是团队的老大
            if Team.objects.filter(user=request.user,document=doc,role=1).count()>0:
                if Team.objects.filter(user=person, document=doc, role=1).count() > 0:#被删除者不能是管理者
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                else:
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
                #请求者是删除本人，且请求者是普通协作者则给创建者发type8消息
                myself = Team.objects.filter(Q(user=request.user),Q(user=person),role=0)
                #请求的人是创建者
                if Team.objects.filter(user=request.user,document=doc,role=1).count()>0: #被删除者不能是管理员（个人文档创建者）
                    if Team.objects.filter(user=person,document=doc,role=1).count()>0:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                    else:
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
                #请求的用户是管理者给被踢人发type9消息
                admin=Team.objects.filter(user=request.user,document=doc,role=1)
                #请求删除用户是自己，并且自己是普通协作者，则给创建者和老大发type8消息
                myself = Team.objects.filter(Q(user=request.user), Q(user=person),role=0)
                #团队
                project=doc.parent_doc
                #请求的用户是团队的老大或文档创建者(管理者)
                if admin.count() > 0:#被删除的不能是管理者或上级协作者
                    if Team.objects.filter(Q(role=1)|Q(role=2),user=person,document=doc).count()>0:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                    else:
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
                if child_doc.create_user== instance.user:  #文档创建者被移除，创建者改为老大
                    Document.objects.filter(id=child_doc.id).update(create_user=doc.create_user)
                #团队文档中被 被移除者 删了的文档，要彻底的删掉。
                if RecycleBin.objects.filter(user=instance.user,document=child_doc).count()>0:
                    child_doc.delete()
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
                if Team.objects.filter(document=child_doc, user=instance.user).count() == 0:
                    Team.objects.create(document=child_doc, user=instance.user,role=2)

        #给老大发2消息
        leader = doc.create_user
        Message.objects.create(user=leader, origin_user=instance.user, document=doc, type=2)


#拒绝邀请
class RefuseInvitationViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
        create:拒绝团队协作，给老大发type10消息
    '''
    queryset = Team.objects.all()
    serializer_class = EditTeamSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.validated_data['document']
        if doc.type == 1:
            leader = doc.create_user
            Message.objects.create(user=leader, origin_user=request.user, document=doc, type=10)
            coworker = get(doc)
            return JsonResponse(coworker, safe=False)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

