# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0015_auto_20150806_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('steps', models.IntegerField(null=True)),
                ('calories', models.FloatField(max_length=9, null=True)),
                ('distances', models.FloatField(max_length=9)),
                ('date', models.DateField()),
                ('last_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to='fitAdmin.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='sport',
            name='user',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]
