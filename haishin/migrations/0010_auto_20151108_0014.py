# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0009_auto_20151107_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.CharField(help_text=b'Ej: SCL, BSAS, ...', max_length=5),
        ),
    ]
