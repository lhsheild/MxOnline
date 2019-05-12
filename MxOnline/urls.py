"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve

from apps.users.views import LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, \
    ModifyPwdView, IndexView
from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget'),
    url(r'^reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset'),
    url(r'^modify/$', ModifyPwdView.as_view(), name='modify'),

    url(r"^users/", include(('apps.users.urls', 'users'), namespace="users")),
    url(r"^org/", include(('apps.organization.urls', 'org'), namespace="org")),
    url(r"^course/", include(('apps.courses.urls', 'course'), namespace="courses")),

    url(r'^captcha/', include('captcha.urls')),  # 验证码
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
]

# 全局404页面配置
handler404 = 'apps.users.views.pag_not_found'
# 全局500页面配置
handler500 = 'apps.users.views.page_error'
