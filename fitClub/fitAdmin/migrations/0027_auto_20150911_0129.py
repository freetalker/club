# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0026_auto_20150909_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderOperLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=200)),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(to='fitAdmin.Order')),
                ('user', models.ForeignKey(to='fitAdmin.User', db_column=b'create_by')),
            ],
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 1, 29, 26, 285834)),
        ),
    ]
