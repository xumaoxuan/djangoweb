# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_sidelink'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SideLink',
        ),
    ]