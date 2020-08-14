from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import Comment,UserCol
from .serializers import CommentSerializer,ColSerializer
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CommentViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """"
    create:创建评论
    destroy:删除评论
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        self.queryset = Comment.objects.filter(create_user=self.request.user)
        return self.queryset


class ColViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    List:用户收藏列表
    create:收藏
    destroy:取消收藏
    """
    queryset = UserCol.objects.all()
    serializer_class = ColSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        self.queryset = UserCol.objects.filter(create_user=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        instance=serializer.save()
        create_user = instance.user
        create_user.collect_num += 1
        create_user.save()


    def perform_destroy(self, instance):
        create_user = instance.user
        create_user.collect_num -= 1
        create_user.save()
        instance.delete()




