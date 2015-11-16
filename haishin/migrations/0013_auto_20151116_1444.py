# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0012_auto_20151116_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishAddon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('dish', models.ForeignKey(to='haishin.Dish')),
            ],
        ),
        migrations.RemoveField(
            model_name='dishaddons',
            name='dish',
        ),
        migrations.DeleteModel(
            name='DishAddons',
        ),
    ]
