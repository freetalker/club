# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitAdmin', '0018_auto_20150906_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=20000)),
                ('cover_path', models.FilePathField(verbose_name=b'/media/kno_cover/')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('hot_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='sportdate',
            name='sport_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 7, 23, 1, 49, 372432)),
        ),
        migrations.AddField(
            model_name='knowledge',
            name='types',
            field=models.ManyToManyField(to='fitAdmin.KnowledgeType'),
        ),
        migrations.AddField(
            model_name='knowledge',
            name='user',
            field=models.ForeignKey(to='fitAdmin.User', db_column=b'create_by'),
        ),
    ]
