# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0027_auto_20150911_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderoperlog',
            old_name='user',
            new_name='actor',
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='last_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 3, 41, 39, 886740)),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 3, 41, 39, 886701)),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 3, 41, 39, 878097)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 3, 41, 39, 878261)),
        ),
    ]
