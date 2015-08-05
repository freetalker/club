# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0007_auto_20150805_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(null=True, upload_to=b'./avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='remark',
            field=models.CharField(default=b'', max_length=300, null=True),
        ),
    ]
