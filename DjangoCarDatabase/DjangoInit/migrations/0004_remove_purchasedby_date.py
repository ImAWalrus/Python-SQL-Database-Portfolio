# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbassignment2', '0003_auto_20171030_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedby',
            name='date',
        ),
    ]
