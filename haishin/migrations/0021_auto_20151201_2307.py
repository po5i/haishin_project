# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0020_auto_20151123_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishaddon',
            name='dish',
            field=models.ForeignKey(related_name='addons', to='haishin.Dish'),
        ),
    ]
