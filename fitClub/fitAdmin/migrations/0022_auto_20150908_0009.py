# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0021_auto_20150907_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledge',
            name='name',
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 8, 0, 9, 6, 955371)),
        ),
    ]
