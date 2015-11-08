# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0010_auto_20151108_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobstatushistory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 12, 46, 48, 94680, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
