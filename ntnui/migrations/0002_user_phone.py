# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntnui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(
                blank=True, max_length=12, verbose_name='phone number'),
        ),
    ]
