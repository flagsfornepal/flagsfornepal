# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0004_auto_20150429_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='email',
            field=models.EmailField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='message',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
