# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0007_auto_20151107_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesscategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'business categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'dish categories'},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='job',
            old_name='swift_api_id',
            new_name='swift_job_id',
        ),
        migrations.AddField(
            model_name='job',
            name='shippify_task_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='delivery_status',
            field=models.CharField(max_length=100, choices=[(b'1', b'Getting ready'), (b'2', b'Pending to assign'), (b'3', b'Pending for shipper response'), (b'4', b'Shipper confirmed'), (b'5', b'Being picked up'), (b'6', b'Being delivered'), (b'7', b'Delivered successfully'), (b'0', b'Cancelled')]),
        ),
    ]
