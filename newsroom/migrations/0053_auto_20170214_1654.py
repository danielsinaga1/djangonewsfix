# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0052_auto_20170207_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='primary_image_size',
            field=models.CharField(default='extra_large', help_text="Choose 'LEAVE' if image size should not be changed.", max_length=20),
        ),
    ]
