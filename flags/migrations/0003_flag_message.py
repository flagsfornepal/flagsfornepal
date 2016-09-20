# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0002_flag_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='message',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]
