# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-05 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('key', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
                ('value', models.TextField()),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Group')),
            ],
        ),
    ]
