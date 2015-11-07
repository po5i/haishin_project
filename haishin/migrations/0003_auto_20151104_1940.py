# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0002_auto_20151030_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='delivery_status',
            field=models.CharField(max_length=100, choices=[(b'Unassigned', b'Unassigned'), (b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'PickedUp', b'PickedUp'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='main_status',
            field=models.CharField(max_length=100, choices=[(b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'Rejected', b'Rejected'), (b'Shipped', b'Shipped'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')]),
        ),
    ]
