# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0014_auto_20150806_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('steps', models.IntegerField()),
                ('calories', models.FloatField(max_length=9)),
                ('distances', models.FloatField(max_length=9)),
                ('last_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to='fitAdmin.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='sportstatic',
            name='user',
        ),
        migrations.RenameField(
            model_name='sport',
            old_name='distance',
            new_name='distances',
        ),
        migrations.RemoveField(
            model_name='sportconf',
            name='edit_time',
        ),
        migrations.AddField(
            model_name='sport',
            name='last_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='SportStatic',
        ),
    ]
