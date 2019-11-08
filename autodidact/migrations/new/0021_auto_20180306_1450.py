# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-06 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autodidact', '0020_auto_20180306_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='name')),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.AddField(
            model_name='session',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='sessions', to='autodidact.Tag'),
        ),
    ]
