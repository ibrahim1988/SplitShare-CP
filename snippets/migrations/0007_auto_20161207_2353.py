# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_remove_trans_transid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('groupcreateId', models.IntegerField(blank=True, default=0, null=True)),
                ('groupuserId', models.IntegerField(blank=True, default=0, null=True)),
                ('groupId', models.IntegerField(blank=True, default=0, null=True)),
                ('groupName', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AlterField(
            model_name='trans',
            name='groupId',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='trans',
            name='transuserId',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
