# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(verbose_name=b'date published')),
                ('image', models.ImageField(upload_to=b'flags/%Y-%B-%d')),
            ],
        ),
    ]
