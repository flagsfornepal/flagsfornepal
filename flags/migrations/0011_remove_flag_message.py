# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0010_auto_20150501_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='message',
        ),
    ]
