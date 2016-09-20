# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0007_auto_20150429_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='location',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
