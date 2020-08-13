"""django_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from.settings import MEDIA_ROOT
from django.views.static import serve
from documents.views import DocEditViewset
from team.views import EditTeamViewset
from users.views import *
router=DefaultRouter()

#使用了自定义的get_quertset方法，所以router.register()中必须加上basename
#创建文集
router.register(r'DocEdit', DocEditViewset, basename='DocEdit')
#获取验证码
router.register(r'codes', SmsCodeViewset, basename='codes')
#用户注册修改信息
router.register(r'users', UserViewset)
#添加团队协作
router.register(r'TeamEdit', EditTeamViewset, basename='TeamEdit')


urlpatterns = [
    path('admin/', admin.site.urls), #django管理站点
    path('api-auth/', include('rest_framework.urls')),  # 若使用可浏览的api,需要登陆注册视图，url可以自定
    url(r'docs/', include_docs_urls(title="django_vue")),
    url(r'^', include(router.urls)),
    path('jwt-auth/', obtain_jwt_token),
    url(r'^login/', obtain_jwt_token),
    path('api-token-auth/', views.obtain_auth_token),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('index/', TemplateView.as_view(template_name='index.html')),
 # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/upload/(?P<path>.*)', serve, {"document_root": 'media/upload/'}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': 'media/upload/', 'show_indexes':True}),
    url(r'qrcode/(.+)$', makeqrcode,name='qrcode')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
