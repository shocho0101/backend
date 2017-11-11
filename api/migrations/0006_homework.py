# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171106_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='api.Group')),
            ],
        ),
    ]