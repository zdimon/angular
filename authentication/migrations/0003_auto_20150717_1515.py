# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_account_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='account',
            old_name='first_name',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
