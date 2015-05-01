# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clozes', '0003_blanktextchunk_last_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=b'button_c.png', upload_to=b'img/', verbose_name=b'Image'),
        ),
    ]
