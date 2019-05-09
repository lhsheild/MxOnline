# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-08 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20190508_1006'),
        ('courses', '0003_auto_20190507_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程机构'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='课程名'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('name', 'course_org')]),
        ),
    ]