# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default=None, upload_to='products'),
            preserve_default=False,
        ),
    ]
