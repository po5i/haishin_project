# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0023_auto_20151202_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetailaddon',
            old_name='detail',
            new_name='job_detail',
        ),
    ]
