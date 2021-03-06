# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_delete_sidelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('left', 'Left Sidebar'), ('right', 'Right Sidebar')], help_text='This is position of the sidebar.', max_length=100, unique=True, verbose_name='Sidebar Position')),
            ],
            options={
                'verbose_name': 'Sidebar',
                'verbose_name_plural': 'Sidebars',
            },
        ),
        migrations.CreateModel(
            name='SidebarWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('widget', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, default=100, null=True)),
                ('sidebar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Sidebar')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'sidebar_widget',
            },
        ),
    ]
