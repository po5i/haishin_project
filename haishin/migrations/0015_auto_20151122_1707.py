# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0014_auto_20151120_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 17, 7, 58, 873826, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='shippify_distance',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippify_price',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
