# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0010_auto_20150806_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportconf',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sportconf',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
