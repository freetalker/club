# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0005_auto_20150805_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
