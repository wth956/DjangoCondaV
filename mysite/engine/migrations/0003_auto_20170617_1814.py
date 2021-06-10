# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20170613_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='photo_url',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
    ]
