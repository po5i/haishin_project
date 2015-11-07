# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0003_auto_20151104_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='town',
            name='country',
        ),
    ]
