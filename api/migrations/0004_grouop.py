# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 03:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171030_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('joincode', models.CharField(max_length=255)),
                ('member', models.ManyToManyField(related_name='Groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]