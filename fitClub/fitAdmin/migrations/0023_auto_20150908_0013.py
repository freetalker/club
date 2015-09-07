# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0022_auto_20150908_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='cover_path',
            field=models.ImageField(null=True, upload_to=b'./covers/'),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='pic_path',
            field=models.ImageField(null=True, upload_to=b'./products/'),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 8, 0, 13, 54, 307562)),
        ),
    ]
