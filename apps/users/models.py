from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.organization.models import CourseOrg


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(("male", '男'), ('female', "女")), default="female", max_length=10)
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default='image/default.png', max_length=100)
    course_org = models.ManyToManyField(to=CourseOrg, verbose_name='课程机构', null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def get_unread_msg_nums(self):
        from apps.operation.models import UserMessage
        user_message = UserMessage.objects.filter(user=self.id, has_read=False)
        return user_message.count()


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加事件')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
