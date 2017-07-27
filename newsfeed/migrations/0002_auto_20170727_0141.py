# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewspiecePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='newsfeed_newspiecepluginmodel', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='newspiece',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='newspiece',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='newspiecepluginmodel',
            name='newspiece',
            field=models.ForeignKey(to='newsfeed.Newspiece'),
        ),
    ]
