# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0008_auto_20150430_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='state',
            field=models.CharField(default=b'new', max_length=10),
        ),
    ]
