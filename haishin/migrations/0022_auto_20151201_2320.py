# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import haishin.models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0021_auto_20151201_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(null=True, upload_to=haishin.models.get_logo_path, blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='average_delivery_time',
            field=models.IntegerField(default=30, help_text=b'En minutos', null=True, blank=True),
        ),
    ]
