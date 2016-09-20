# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0009_flag_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flag',
            old_name='title',
            new_name='tagline',
        ),
        migrations.AddField(
            model_name='flag',
            name='thumbnail',
            field=models.ImageField(upload_to=b'flags/%Y/%B/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='image',
            field=models.ImageField(upload_to=b'flags/%Y/%B/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
