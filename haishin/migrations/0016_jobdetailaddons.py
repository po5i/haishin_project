# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0015_auto_20151122_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetailAddons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('addon', models.ForeignKey(to='haishin.DishAddon')),
                ('detail', models.ForeignKey(to='haishin.JobDetail')),
            ],
        ),
    ]
