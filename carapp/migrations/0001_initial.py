# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=50, verbose_name='口令')),
                ('passwd2', models.CharField(max_length=50, verbose_name='确认口令')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=12, verbose_name='电话')),
                ('img', models.ImageField(upload_to='user/images', verbose_name='头像')),
            ],
            options={
                'verbose_name': '二手车管理',
                'verbose_name_plural': '二手车管理',
                'db_table': 's_car',
            },
        ),
    ]
