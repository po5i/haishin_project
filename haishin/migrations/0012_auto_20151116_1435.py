# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import haishin.models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0011_jobstatushistory_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishAddons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='DishCustomization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('options', models.TextField(help_text=b'Opciones separadas con coma', null=True, blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='jobstatushistory',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['city__country__name', 'city__name', 'name']},
        ),
        migrations.AddField(
            model_name='business',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='business',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=haishin.models.get_business_cover_path, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='friday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='friday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='monday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='monday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='price_range',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business',
            name='saturday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='saturday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='sunday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='sunday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='thursday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='thursday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='tuesday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='tuesday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='wednesday_closes',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='wednesday_opens',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(null=True, upload_to=haishin.models.get_city_path, blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='available_from',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='available_to',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.CharField(help_text=b'Ej: SCL, CABA, ...', max_length=5),
        ),
        migrations.AddField(
            model_name='dishcustomization',
            name='dish',
            field=models.ForeignKey(to='haishin.Dish'),
        ),
        migrations.AddField(
            model_name='dishaddons',
            name='dish',
            field=models.ForeignKey(to='haishin.Dish'),
        ),
    ]
