# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0013_auto_20151116_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishAddonCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('maximum', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'dish addon categories',
            },
        ),
        migrations.AddField(
            model_name='dishaddon',
            name='category',
            field=models.ForeignKey(default=1, to='haishin.DishAddonCategory'),
            preserve_default=False,
        ),
    ]
