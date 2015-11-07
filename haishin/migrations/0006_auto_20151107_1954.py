# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0005_city_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name_plural': 'businesses'},
        ),
        migrations.AlterModelOptions(
            name='businesscategory',
            options={'verbose_name_plural': 'business categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'verbose_name_plural': 'dish categories'},
        ),
        migrations.AlterField(
            model_name='business',
            name='admin',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='business',
            name='discount',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
