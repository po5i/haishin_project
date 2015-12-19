# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0005_country_minimum_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='currency',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'braintree', b'braintree'), (b'stripe', b'stripe'), (b'manual', b'manual')]),
        ),
    ]
