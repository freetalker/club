# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0024_auto_20150908_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cell_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 9, 0, 39, 45, 177479)),
        ),
    ]
