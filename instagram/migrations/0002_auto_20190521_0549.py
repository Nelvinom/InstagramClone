# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
    ]
