# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0003_auto_20151211_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='slug',
            field=models.SlugField(default='aa', help_text=b'Se va a generar automaticamente', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(default='vv', help_text=b'Se va a generar automaticamente', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='url',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
