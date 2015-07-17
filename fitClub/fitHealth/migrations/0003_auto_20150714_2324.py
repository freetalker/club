# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitHealth', '0002_auto_20150705_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('join_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('descriptipn', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='last_login_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='MemberLevel',
            field=models.ForeignKey(related_name='level_id', to='fitHealth.MemberLevel', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='User',
            field=models.ForeignKey(related_name='user_id', to='fitHealth.User'),
        ),
    ]
