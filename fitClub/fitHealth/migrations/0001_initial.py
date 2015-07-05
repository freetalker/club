# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loginname', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('realname', models.CharField(max_length=20)),
                ('sex', models.IntegerField(choices=[(1, b'male'), (2, b'female')])),
                ('age', models.IntegerField(null=True)),
                ('birthday', models.DateField()),
                ('company', models.CharField(max_length=50, null=True)),
                ('job', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('weixin', models.CharField(max_length=20, null=True)),
                ('qq', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('identity', models.CharField(max_length=18, null=True)),
                ('create_time', models.DateTimeField()),
                ('create_by', models.IntegerField()),
                ('isActive', models.BooleanField()),
                ('lastLoginTime', models.DateTimeField(null=True)),
                ('lastLoginIp', models.CharField(max_length=40)),
            ],
        ),
    ]
