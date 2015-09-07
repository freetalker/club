# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0020_auto_20150907_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='author',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 7, 23, 53, 21, 165877)),
        ),
    ]
