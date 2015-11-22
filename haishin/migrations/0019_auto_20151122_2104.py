# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0018_auto_20151122_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='recipient_latitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='recipient_longitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
