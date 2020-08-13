from random import choice

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import  get_user_model
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, mixins, viewsets, authentication, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
# from users.models import UserProfile, UserSerializer
from django.shortcuts import render,redirect
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django_filters.rest_framework import DjangoFilterBackend

from django_vue.settings import APIKEY
from utils.yunpian import YunPian
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly




class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = RegSerializers
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)#authentication.SessionAuthentication
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ('id',)

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        elif self.action=='partial_update':
            return UserUpdateSerializer
        elif self.action == "create":
            return RegSerializers
        elif self.action == "list":
            return OtherUserDetailSerializer
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        if "password" in request.data:
            request.data['password'] = make_password(request.data['password'])
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data = request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


def delete_user(request):
    user_id = request.GET.get('user_id')
    psw = request.GET.get('password')
    User.objects.filter(id=user_id, password=psw).delete()
    return redirect('/index/')


# 发送短信验证码
class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializer

    # 生成四位数字的验证码
    def generate_code(self):
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    # 重写 create 方法
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 验证后即可取出数据
        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 确认无误后需要保存数据库中
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO
def  makeqrcode(request,data):
    # print(request.get_host()+'/'+data+'/')
    url = request.get_host()+'/'+data+'/'
    img = qrcode.make(url)      #传入网址计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
    response = HttpResponse(image_stream, content_type="image/jpg")  #将二维码数据返回到页面
    return response

