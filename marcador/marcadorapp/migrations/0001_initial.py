# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('url', models.URLField()),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(verbose_name='public', default=True)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='bookmarks', verbose_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='marcadorapp.Tag'),
        ),
    ]
