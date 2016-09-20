# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
        ),
    ]
