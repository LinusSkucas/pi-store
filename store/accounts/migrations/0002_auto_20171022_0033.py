# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packages_installs',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
