# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-26 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_fs', '0002_convert_localfs'),
        ('pootle_store', '0032_fix_empty_wordcounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='file',
        ),
    ]
