# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitHealth', '0004_auto_20150714_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login_ip',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
