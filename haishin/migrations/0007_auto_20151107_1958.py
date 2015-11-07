# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0006_auto_20151107_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(to='haishin.DishCategory'),
        ),
    ]
