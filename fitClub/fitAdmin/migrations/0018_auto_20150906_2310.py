# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0017_auto_20150806_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportdetail',
            old_name='distance',
            new_name='distances',
        ),
        migrations.AlterField(
            model_name='alarm',
            name='alarm_time',
            field=models.TimeField(default=b'22:00:00'),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='calories',
            field=models.FloatField(default=0, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='distances',
            field=models.FloatField(default=0, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 6, 23, 10, 22, 618135)),
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='steps',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sportdetail',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sportdetail',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sportstat',
            name='calories',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='sportstat',
            name='distances',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='sportstat',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sportstat',
            name='steps',
            field=models.IntegerField(default=0),
        ),
    ]
