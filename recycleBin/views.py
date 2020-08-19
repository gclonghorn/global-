from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework import status, mixins, viewsets, authentication,filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from django.http import JsonResponse
from team.models import Team
from rest_framework.response import Response
from django.db.models import Q

class RecycleBinViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = RecycleBin.objects.all()
    serializer_class = RecycleDocSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    ordering_fields = ('modify_time',)
    def get_queryset(self):
        ids=[]
        recycles=RecycleBin.objects.filter(user=self.request.user)
        for recycle in recycles:
            if recycle.document.type==0 and recycle.document.parent_doc!=None:
                pass
            else:
                ids.append(recycle.document.id)
        return RecycleBin.objects.filter(document_id__in=ids)


class Recall(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class=RecycleEditSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    #从回收站还原
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status=1 #恢复到发布状态
        instance.save()
        RecycleBin.objects.get(document_id=instance.id).delete()
        if instance.type == 1:  #团队被恢复时团队的下属文档也要被恢复
            child_docs_list = Document.objects.filter(parent_doc=instance)  # 项目下属文档
            for child_doc in child_docs_list:
                child_doc.status=1
                child_doc.save()
        '''
        res = {"code": None, "data": None}
        res["code"] = 200
        res['data'] = "success"
        '''
        return Response(status=status.HTTP_200_OK)

class Pack( mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RecycleEditSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    # 从回收站删除
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        RecycleBin.objects.get(document_id=instance.id).delete()
        if instance.type == 1:  #团队被彻底删除团队的下属文档也要被彻底删除
            child_docs_list = Document.objects.filter(parent_doc=instance)  # 项目下属文档
            for child_doc in child_docs_list:
                child_doc.delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
#全部还原
class AllRecall(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class=RecycleEditSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    def list(self, request, *args, **kwargs):
        recycles=RecycleBin.objects.all()
        docs = []
        for recycle in recycles:
            docs.append(recycle.document)
        for doc in docs:
            doc.status=1
            doc.save()
            if doc.type == 1:  # 团队被恢复时团队的下属文档也要被恢复
                child_docs_list = Document.objects.filter(parent_doc=doc)  # 项目下属文档
                for child_doc in child_docs_list:
                    child_doc.status = 1
                    child_doc.save()
        RecycleBin.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

#全部删除
class AllPack(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class=RecycleEditSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    def list(self, request, *args, **kwargs):
        recycles=RecycleBin.objects.all()
        docs=[]
        for recycle in recycles:
            docs.append(recycle.document)
        for doc in docs:
            if doc.type == 1:  # 团队被彻底删除团队的下属文档也要被彻底删除
                child_docs_list = Document.objects.filter(parent_doc=doc)  # 项目下属文档
                for child_doc in child_docs_list:
                    child_doc.delete()
            doc.delete()
        RecycleBin.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

