# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0002_auto_20150727_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default=datetime.datetime(2015, 7, 30, 9, 26, 26, 191379), upload_to=b'./upload/'),
            preserve_default=False,
        ),
    ]
