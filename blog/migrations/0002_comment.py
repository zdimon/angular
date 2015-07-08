# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=50, verbose_name=b'Author')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(verbose_name=b'Content', blank=True)),
                ('post', models.ForeignKey(verbose_name=b'Topic', to='blog.Post')),
            ],
        ),
    ]
