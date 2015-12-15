# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0004_auto_20151211_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='minimum_order',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
