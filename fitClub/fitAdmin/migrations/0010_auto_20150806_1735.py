# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0009_auto_20150805_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportconf',
            name='distances',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='sportconf',
            name='calories',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='sportconf',
            name='steps',
            field=models.IntegerField(default=0),
        ),
    ]
