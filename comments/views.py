from rest_framework import viewsets
from rest_framework import mixins
from .models import Comment
from team.models import *
from message.models import *
from .serializers import *
from documents.serializers import DocListSerializer
from  rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
# Create your views here.
class CommentViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """"
    create:
    创建评论
    destroy:
    删除评论
    """
    queryset = Comment.objects.all()
    serializer_class = CommentEditSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    #看到文章即可创建
    def perform_create(self, serializer):
        instance=serializer.save()
        doc=instance.document #被评论文档对象
        author=doc.create_user #文档创建者
        if doc.parent_doc == None:boss=None
        else:boss=doc.parent_doc.create_user #老大
        parentcomment=instance.reply_comment#父评论
        print(parentcomment)
        # 7:评论被回复（给被回复的评论人发）
        if parentcomment != None:   #回复评论
            Message.objects.create(user=parentcomment.author, origin_user=instance.author, document=doc, type=7)
        # 6:文档被评论（给被评论的文档的创建者+协作者发）
        elif boss == None:   #评论个人文档
            Message.objects.create(user=author, origin_user=instance.author, document=doc, type=6)
        else: #评论团队文档
            Message.objects.create(user=author, origin_user=instance.author, document=doc, type=6)
            Message.objects.create(user=boss, origin_user=instance.author, document=doc, type=6)
    #评论创建者或文档创建者可删除评论
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        doc=instance.document
        if Document.objects.filter(id=doc.id,create_user=request.user).count()>0 or\
            Comment.objects.filter(id=instance.id,author=request.user).count()>0:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else: return Response(status=status.HTTP_401_UNAUTHORIZED)
    def perform_destroy(self, instance):
        instance.delete()

class CollectViewset(mixins.DestroyModelMixin,mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:收藏
    """
    queryset = Collect.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)


class CollectList(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    list:我的收藏
    '''
    queryset = Document.objects.all()
    serializer_class = DocListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # 被删除的文档不展示
    def get_queryset(self):
        mycollects = Collect.objects.filter(author=self.request.user)
        ids=[]
        for collect in mycollects:
            ids.append(collect.document_id)
        self.queryset = Document.objects.filter(~Q(status=2),Q(id__in=ids))
        return self.queryset

class CancelCollect(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def retrieve(self, request, *args, **kwargs):
           instance = self.get_object()
           Collect.objects.get(author=request.user,document=instance).delete()
           return Response(status=status.HTTP_204_NO_CONTENT)