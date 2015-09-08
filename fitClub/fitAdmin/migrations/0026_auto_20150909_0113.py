# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0025_auto_20150909_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 9, 1, 13, 24, 663277)),
        ),
    ]
