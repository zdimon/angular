# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=30, verbose_name=b'Name', db_index=True, blank=True)),
                ('content', models.TextField(max_length=30, null=True, blank=True)),
                ('name_slug', models.CharField(max_length=250, verbose_name=b'Name slug', blank=True)),
            ],
        ),
    ]
