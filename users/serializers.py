import code

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User
from rest_framework.validators import UniqueTogetherValidator

#注册
class RegSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=256, min_length=4, write_only=True)
    mobile = serializers.CharField(max_length=11, min_length=11)
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 })
    def validate(self, attrs):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["mobile"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]  # 时间倒叙排序后的的第一条就是最新的一条
            if last_record.code != self.initial_data["code"]:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")
        if attrs['pwd2'] != attrs['password']:
            raise ValidationError('两次密码输入不一致')
        del attrs['pwd2']
        del attrs["code"]  # 删除无用字段
 		#对密码进行加密 make_password
        attrs['password'] = make_password(attrs['password'])
        return attrs
    class Meta:
        model = User
        fields=('username', 'password', 'pwd2', 'mobile', 'code')





from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from datetime import datetime
from datetime import timedelta
import re
User = get_user_model()


#用于粉丝概要信息
class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')

class OtherUserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("username", "mobile", "email", 'id', 'head')#'posts'
        #ids关注者 usernames粉丝
class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("username", "mobile", "email", 'password','id', 'head')
        #ids关注者 usernames粉丝
class UserUpdateSerializer(serializers.ModelSerializer):
    """
    用户修改信息序列化类
    """
    # def validate(self, attrs):
    #     attrs['password'] = make_password(self.initial_data["password"])
    #     return attrs
    class Meta:
        model = User
        fields = ("username", "mobile", "email", 'password','id','head')#'posts'
        #ids关注者 usernames粉丝

class SearchSerializer(serializers.ModelSerializer):
    """
    用户搜索序列化类
    """
    class Meta:
        model = User
        fields = ('id', 'last_name')



import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from .models import VerifyCode
from django_vue.settings import REGEX_MOBILE

User = get_user_model()
# 手机验证序列化组件
# 不使用 ModelSerializer, 并不需要所有的字段, 会有麻烦
class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    # 验证手机号码
    # validate_ + 字段名 的格式命名
    def validate_mobile(self, mobile):

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        # 当前时间减去一分钟( 倒退一分钟 ), 然后发送时间要大于这个时间, 表示还在一分钟内
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")
        return mobile



