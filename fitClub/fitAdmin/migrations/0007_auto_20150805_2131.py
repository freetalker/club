# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0006_auto_20150805_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
