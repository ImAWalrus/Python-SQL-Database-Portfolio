# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbassignment2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='fitscar',
            name='make',
        ),
        migrations.AlterField(
            model_name='fitscar',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts_that_fit', to='dbassignment2.Car'),
        ),
    ]
