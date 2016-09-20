# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0011_remove_flag_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='flagReason',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
