# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_auto_20170617_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='detail',
            field=models.CharField(blank=True, max_length=6000),
        ),
    ]
