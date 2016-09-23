# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-23 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Costo total de la orden')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Delivered'), (2, 'Rejected')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad en gramos')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Resource')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(through='restaurants.OrderItem', to='products.Resource'),
        ),
        migrations.AddField(
            model_name='order',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
    ]
