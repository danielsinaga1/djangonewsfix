# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-27 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='album',
            field=models.ManyToManyField(blank=True, to='gallery.Album'),
        ),
    ]
