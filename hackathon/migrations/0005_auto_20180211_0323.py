# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_auto_20180211_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='recording',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hackathon.Recordings'),
        ),
    ]
