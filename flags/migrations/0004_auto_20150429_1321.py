# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0003_flag_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flag',
            name='image',
            field=models.ImageField(upload_to=b'flags/%Y/%B/%d'),
        ),
    ]
