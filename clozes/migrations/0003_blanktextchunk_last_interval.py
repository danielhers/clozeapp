# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clozes', '0002_auto_20150430_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='blanktextchunk',
            name='last_interval',
            field=models.IntegerField(default=1),
        ),
    ]
