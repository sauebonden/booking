# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
