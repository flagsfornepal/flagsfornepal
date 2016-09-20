# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0005_auto_20150429_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='title',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
