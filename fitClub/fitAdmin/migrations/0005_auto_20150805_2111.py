# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0004_auto_20150730_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remark',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 21, 11, 6, 421557)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 21, 11, 6, 419583)),
        ),
    ]
