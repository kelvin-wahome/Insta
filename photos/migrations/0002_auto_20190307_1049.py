# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
    ]
