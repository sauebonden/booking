# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180313_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='group',
            field=models.CharField(blank=True, choices=[('', '---------')], max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='title',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('gym ', 'GYM'), ('football field', 'FOOTBALL FIELD'), ('volleyball grounds', 'VOLLEYBALL GROUNDS')], default='gym', max_length=200),
        ),
    ]