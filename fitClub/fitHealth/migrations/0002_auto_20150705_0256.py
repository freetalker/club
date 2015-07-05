# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitHealth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastLoginIp',
            new_name='last_login_ip',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastLoginTime',
            new_name='last_login_time',
        ),
    ]
