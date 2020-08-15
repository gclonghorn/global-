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
        self.queryset=RecycleBin.objects.filter(user=self.request.user).order_by('-delete_time')
        return self.queryset

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
        res = {"code": None, "data": None}
        res["code"] = 200
        res['data'] = "success"
        return JsonResponse(res, safe=False)

class Pack( mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RecycleEditSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    # 从回收站删除
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        RecycleBin.objects.get(document_id=instance.id).delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

