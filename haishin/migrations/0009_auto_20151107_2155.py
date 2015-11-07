# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0008_auto_20151107_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='business',
            name='city',
        ),
        migrations.RemoveField(
            model_name='business',
            name='country',
        ),
        migrations.AlterField(
            model_name='business',
            name='discount',
            field=models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='latitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='longitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
