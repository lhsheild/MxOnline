from datetime import datetime

from django.db import models

from apps.courses import models as course_models
from apps.users import models as user_models
from apps.organization import models as org_models


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(user_models.UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(course_models.Course, verbose_name='课程', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(user_models.UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.CharField(choices=((1, '课程'), (2, '课程机构'), (3, '教师')), max_length=4)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='接收用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(user_models.UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(course_models.Course, verbose_name='课程', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
