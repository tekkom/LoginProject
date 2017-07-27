# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
=======
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
>>>>>>> 5249059a14ba7d952bcc0c70c2c6adab0204d499
                ('gName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
=======
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
>>>>>>> 5249059a14ba7d952bcc0c70c2c6adab0204d499
                ('email', models.CharField(max_length=50)),
                ('uName', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('group', models.ForeignKey(to='users.Group')),
            ],
        ),
    ]
