# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0016_auto_20150806_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportdate',
            old_name='date',
            new_name='sport_date',
        ),
    ]
