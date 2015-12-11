# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0002_auto_20151206_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='last_status',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='last_update',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
