# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitHealth', '0005_auto_20150714_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_id', models.IntegerField(choices=[(101, b'\xe6\xad\xa5\xe6\x95\xb0'), (102, b'\xe5\x85\xac\xe9\x87\x8c\xe6\x95\xb0'), (103, b'\xe7\x82\xb9\xe6\x95\xb0'), (104, b'\xe5\x8d\xa1\xe8\xb7\xaf\xe9\x87\x8c'), (201, b'\xe7\x9d\xa1\xe7\x9c\xa0'), (202, b'\xe4\xbd\x93\xe9\x87\x8d'), (203, b'\xe8\xa1\x80\xe5\x8e\x8b')])),
                ('critical', models.IntegerField()),
                ('alarm_time', models.TimeField()),
                ('alarm_channel', models.IntegerField(choices=[(1, b'\xe5\xba\x94\xe7\x94\xa8'), (2, b'\xe5\xbe\xae\xe4\xbf\xa1'), (3, b'\xe7\x9f\xad\xe4\xbf\xa1'), (4, b'\xe9\x82\xae\xe4\xbb\xb6')])),
            ],
            options={
                'db_table': 'alarm',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('mac', models.CharField(max_length=30, null=True)),
                ('device_user', models.CharField(max_length=20)),
                ('device_token', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='DeviceBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'device_brand',
            },
        ),
        migrations.CreateModel(
            name='DeviceUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bind_time', models.DateField()),
                ('status', models.IntegerField(choices=[(1, b'\xe6\xbf\x80\xe6\xb4\xbb'), (2, b'\xe4\xb8\xa2\xe5\xa4\xb1'), (3, b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('device', models.ForeignKey(to='fitHealth.Device')),
            ],
            options={
                'db_table': 'device_user',
            },
        ),
        migrations.CreateModel(
            name='HealthBloodPress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('low_pressure', models.FloatField()),
                ('high_pressure', models.FloatField()),
            ],
            options={
                'db_table': 'health_bp',
            },
        ),
        migrations.CreateModel(
            name='HealthSleep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin_time', models.DateTimeField()),
                ('auto_detected', models.BooleanField()),
                ('duration', models.IntegerField(null=True)),
                ('details', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'health_sleep',
            },
        ),
        migrations.CreateModel(
            name='HealthWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('weight', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'health_weight',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_code', models.CharField(max_length=10)),
                ('total_pay', models.FloatField(max_length=9)),
                ('status', models.IntegerField(choices=[(1, b'\xe5\xb7\xb2\xe4\xb8\x8b\xe5\x8d\x95'), (2, b'\xe5\xb7\xb2\xe7\xa1\xae\xe8\xae\xa4'), (3, b'\xe5\xb7\xb2\xe5\x8f\x91\xe8\xb4\xa7'), (4, b'\xe5\xb7\xb2\xe6\x94\xb6\xe8\xb4\xa7')])),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_price', models.FloatField()),
                ('product_price', models.FloatField()),
                ('number', models.FloatField()),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(to='fitHealth.Order')),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
                ('discount', models.FloatField()),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_path', models.FilePathField(path=b'/media/pro_img/')),
                ('seq', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='fitHealth.Product')),
            ],
            options={
                'db_table': 'product_picture',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('points', models.IntegerField()),
                ('steps', models.IntegerField(null=True)),
                ('calories', models.FloatField(max_length=9, null=True)),
                ('distance', models.FloatField(max_length=9)),
            ],
            options={
                'db_table': 'sport',
            },
        ),
        migrations.CreateModel(
            name='SportConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('steps', models.IntegerField()),
                ('calories', models.FloatField(max_length=9)),
                ('create_time', models.DateTimeField()),
                ('edit_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'sport_conf',
            },
        ),
        migrations.CreateModel(
            name='SportDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duration', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('points', models.IntegerField(null=True)),
                ('steps', models.IntegerField(null=True)),
                ('calories', models.FloatField(max_length=9, null=True)),
                ('distance', models.FloatField(max_length=9)),
            ],
            options={
                'db_table': 'sport_detail',
            },
        ),
        migrations.CreateModel(
            name='SportStatic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('steps', models.IntegerField()),
                ('calories', models.FloatField(max_length=9)),
                ('distance', models.FloatField(max_length=9)),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'sport_static',
            },
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(to='fitHealth.MemberLevel', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterModelTable(
            name='memberlevel',
            table='member_level',
        ),
        migrations.AddField(
            model_name='sportstatic',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='sportdetail',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='sportconf',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='sport',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(to='fitHealth.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='fitHealth.User', db_column=b'create_by'),
        ),
        migrations.AddField(
            model_name='healthweight',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='healthsleep',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='healthbloodpress',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='deviceuser',
            name='user',
            field=models.ForeignKey(to='fitHealth.User'),
        ),
        migrations.AddField(
            model_name='device',
            name='brand',
            field=models.ForeignKey(to='fitHealth.DeviceBrand'),
        ),
    ]
