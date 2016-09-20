# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0012_flag_flagreason'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='original',
            field=models.ImageField(upload_to=b'flags/%Y/%B/%d', blank=True),
        ),
    ]
