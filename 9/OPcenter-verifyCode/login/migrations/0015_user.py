# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0014_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_pw', models.CharField(max_length=128, unique=True)),
                ('no_login', models.IntegerField(default='1')),
            ],
        ),
    ]
