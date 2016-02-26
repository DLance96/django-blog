# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 16:56
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160226_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='section',
            name='img',
            field=models.ImageField(default='', upload_to=blog.models.post_dir_path),
        ),
    ]
