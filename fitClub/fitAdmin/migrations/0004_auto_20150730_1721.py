# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 17, 21, 53, 917336)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 17, 21, 53, 919219)),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(upload_to=b'./avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
