# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('body', models.TextField()),
                ('created_at', models.DateField(db_index=True, auto_now_add=True)),
                ('updated_at', models.DateField()),
            ],
        ),
    ]
