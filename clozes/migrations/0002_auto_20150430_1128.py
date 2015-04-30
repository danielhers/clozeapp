# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clozes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='e_factor',
        ),
        migrations.RemoveField(
            model_name='textchunk',
            name='e_factor',
        ),
        migrations.RemoveField(
            model_name='textchunk',
            name='next_appearance',
        ),
        migrations.AddField(
            model_name='textchunk',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='BlankTextChunk',
            fields=[
                ('textchunk_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='clozes.TextChunk')),
                ('next_appearance', models.DateField()),
                ('e_factor', models.IntegerField()),
            ],
            bases=('clozes.textchunk',),
        ),
    ]
