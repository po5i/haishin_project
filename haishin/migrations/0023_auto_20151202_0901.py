# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0022_auto_20151201_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetailAddon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('addon', models.ForeignKey(to='haishin.DishAddon')),
                ('detail', models.ForeignKey(related_name='addons', to='haishin.JobDetail')),
            ],
        ),
        migrations.RemoveField(
            model_name='jobdetailaddons',
            name='addon',
        ),
        migrations.RemoveField(
            model_name='jobdetailaddons',
            name='detail',
        ),
        migrations.AlterField(
            model_name='business',
            name='friday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='friday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='monday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='monday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='saturday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='saturday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='sunday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='sunday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='thursday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='thursday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='tuesday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='tuesday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='wednesday_closes',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='wednesday_opens',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='available_from',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='available_to',
            field=models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='JobDetailAddons',
        ),
    ]
