# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20171118_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
