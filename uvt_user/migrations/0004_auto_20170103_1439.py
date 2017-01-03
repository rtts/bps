# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uvt_user', '0003_fix_empty_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='uvtuser',
            name='emplId',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='uvtuser',
            name='last_name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
