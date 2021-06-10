# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='電影')),
                ('detail', models.CharField(max_length=6000, default='')),
                ('photo_url', models.CharField(max_length=200, default='')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='給個評分吧!')),
                ('pub_date', models.DateTimeField(verbose_name='評分時間')),
                ('comment', models.CharField(max_length=200, blank=True, verbose_name='給個留言')),
                ('movie', models.ForeignKey(to='engine.Movie', verbose_name='電影')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='評分者')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
