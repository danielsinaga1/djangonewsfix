# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-07 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20161108_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
    ]
