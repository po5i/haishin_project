# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='rejected_message',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shipper_information',
            field=models.TextField(null=True, blank=True),
        ),
    ]
