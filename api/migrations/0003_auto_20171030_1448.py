# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171030_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]
