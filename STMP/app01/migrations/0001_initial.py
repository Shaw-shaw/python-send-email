# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-12 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('is_live', models.BooleanField(default=0)),
                ('token', models.CharField(max_length=256)),
            ],
        ),
    ]