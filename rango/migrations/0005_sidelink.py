# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('titlelink', models.CharField(max_length=128)),
            ],
        ),
    ]