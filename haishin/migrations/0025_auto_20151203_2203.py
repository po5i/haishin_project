# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('haishin', '0024_auto_20151202_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=100)),
                ('card', models.CharField(max_length=10, null=True, blank=True)),
                ('last', models.CharField(max_length=5, null=True, blank=True)),
                ('paypal_email', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='main_status',
            field=models.CharField(max_length=100, choices=[(b'Draft', b'Draft'), (b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'Rejected', b'Rejected'), (b'Shipped', b'Shipped'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')]),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='job',
            field=models.ForeignKey(to='haishin.Job'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
