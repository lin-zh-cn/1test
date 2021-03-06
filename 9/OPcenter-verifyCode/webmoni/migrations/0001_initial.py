# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('http_code', models.IntegerField(null=True)),
                ('namelookup_time', models.IntegerField(null=True)),
                ('connect_time', models.IntegerField(null=True)),
                ('pretransfer_time', models.IntegerField(null=True)),
                ('starttransfer_time', models.IntegerField(null=True)),
                ('total_time', models.IntegerField(null=True)),
                ('size_download', models.IntegerField(null=True)),
                ('header_size', models.IntegerField(null=True)),
                ('speed_download', models.IntegerField(null=True)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='monitordata',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmoni.Node'),
        ),
        migrations.AddField(
            model_name='monitordata',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmoni.DomainName'),
        ),
        migrations.AddField(
            model_name='event_log',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmoni.Event_Type'),
        ),
        migrations.AddField(
            model_name='event_log',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmoni.Node'),
        ),
        migrations.AddField(
            model_name='event_log',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webmoni.DomainName'),
        ),
        migrations.AddField(
            model_name='domainname',
            name='project_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webmoni.Project'),
        ),
        migrations.AddField(
            model_name='domainname',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webmoni.Event_Type'),
        ),
    ]
