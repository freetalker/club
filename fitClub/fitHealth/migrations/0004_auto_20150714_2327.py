# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitHealth', '0003_auto_20150714_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='MemberLevel',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='User',
            new_name='user',
        ),
    ]
