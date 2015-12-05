# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0026_auto_20151205_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='shipping',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='about',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='privacy',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='terms_conditions',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
    ]
