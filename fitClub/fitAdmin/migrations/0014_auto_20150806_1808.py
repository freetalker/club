# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0013_auto_20150806_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportconf',
            name='edit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
