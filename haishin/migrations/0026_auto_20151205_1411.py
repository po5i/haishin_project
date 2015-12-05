# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0025_auto_20151203_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='about',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='privacy',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='terms_conditions',
            field=models.TextField(null=True, blank=True),
        ),
    ]
