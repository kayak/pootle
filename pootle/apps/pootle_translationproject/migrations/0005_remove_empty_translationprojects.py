# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-08 19:40
from __future__ import unicode_literals

from django.db import migrations


def drop_empty_translationprojects(apps, schema_editor):
    """Drop TPs with no directories."""
    Directory = apps.get_model("pootle_app.Directory")
    TP = apps.get_model("pootle_translationproject.TranslationProject")

    for tp in TP.objects.all():
        if not Directory.objects.filter(pootle_path=tp.pootle_path).exists():
            tp.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_translationproject', '0004_add_reverse_tp_idx'),
        ('pootle_data', '0006_add_cascade_deletes'),
        ('pootle_app', '0015_add_tp_path_idx'),
    ]

    operations = [
        migrations.RunPython(drop_empty_translationprojects),
    ]