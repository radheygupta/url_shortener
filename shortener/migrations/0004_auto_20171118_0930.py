# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20171118_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
