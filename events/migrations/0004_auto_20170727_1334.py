# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170727_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
