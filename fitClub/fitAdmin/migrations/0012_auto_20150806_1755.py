# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0011_auto_20150806_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberlevel',
            old_name='descriptipn',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='sportconf',
            name='user',
            field=models.ForeignKey(to='fitAdmin.User', unique=True),
        ),
    ]
