# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 11:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.TaskType'),
        ),
        migrations.AddField(
            model_name='weeklyschedule',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Task'),
        ),
    ]
