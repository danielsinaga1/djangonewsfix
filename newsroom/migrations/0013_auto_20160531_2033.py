# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0012_article_letters_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments_on',
            field=models.BooleanField(default=False),
        ),
    ]