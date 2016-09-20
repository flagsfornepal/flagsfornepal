# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0006_flag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
