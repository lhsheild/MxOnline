from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市', unique=True)
    desc = models.CharField(max_length=200, verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='封面图')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市', on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=(("pxjg", u"培训机构"), ("gx", u"高校"), ("gr", u"个人"),),
                                verbose_name=u"机构类别", default="pxjg")
    students = models.IntegerField("学习人数", default=0)
    course_nums = models.IntegerField("课程数", default=0)
    tag = models.CharField('机构标签', max_length=10, default='全国知名')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
        unique_together = (('name', 'city'),)

    def __str__(self):
        return self.name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='教师名')
    work_year = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    teacher_age = models.IntegerField(verbose_name='年龄', default=25)
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        unique_together = (('org', 'name'),)

    def __str__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()
