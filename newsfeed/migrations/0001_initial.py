# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newspiece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=64)),
                ('content', models.TextField(default='')),
            ],
        ),
    ]
