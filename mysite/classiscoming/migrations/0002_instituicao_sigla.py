# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classiscoming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='sigla',
            field=models.CharField(default='sigla', max_length=300),
            preserve_default=False,
        ),
    ]