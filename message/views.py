from django.http import JsonResponse
from rest_framework import mixins, viewsets, authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from documents.models import Document
from message.models import Message
from message.serializers import MessageSerializer, UpdateSerializer, AllUpdateSerializer
from team.models import Team
from users.models import User


class MessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """"
    destroy:
    删除单个消息
    update:
    单个消息已读
    list:
    查看未读消息
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateSerializer
        return MessageSerializer

    #返回未读消息
    def list(self, request, *args, **kwargs):
        self.queryset = Message.objects.filter(status=0, user=request.user)
        queryset = self.filter_queryset(self.queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    #删除指定消息
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)



class AllMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """"
    destroy:
    删除全部消息
    update:
    全部消息已读
    list:
    查看全部消息
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'update':
            return AllUpdateSerializer
        return MessageSerializer

    # 返回全部消息
    def list(self, request, *args, **kwargs):
        self.queryset = Message.objects.filter(user=request.user)
        queryset = self.filter_queryset(self.queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    #删除全部消息
    def destroy(self, request, *args, **kwargs):
        Message.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)

    #全部已读功能
    def update(self, request, *args, **kwargs):
        Message.objects.filter(user=request.user).update(status=1)
        return Response(status=status.HTTP_200_OK)


