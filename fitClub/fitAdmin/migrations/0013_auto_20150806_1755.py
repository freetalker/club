# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0012_auto_20150806_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportconf',
            name='user',
            field=models.OneToOneField(to='fitAdmin.User'),
        ),
    ]
