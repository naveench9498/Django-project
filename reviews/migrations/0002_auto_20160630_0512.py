# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='wine',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]