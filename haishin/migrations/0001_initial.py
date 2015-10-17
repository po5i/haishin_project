# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import haishin.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=haishin.models.get_business_path, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('admin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tags', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('published', models.BooleanField(default=True)),
                ('business', models.ForeignKey(to='haishin.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('swift_api_id', models.CharField(max_length=512, null=True, blank=True)),
                ('payment_reference_id', models.CharField(max_length=512, null=True, blank=True)),
                ('recipient_name', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_address', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_phone', models.CharField(max_length=100, null=True, blank=True)),
                ('main_status', models.CharField(max_length=100, choices=[(b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'Delivered', b'Delivered'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')])),
                ('delivery_status', models.CharField(max_length=100, choices=[(b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'PickedUp', b'PickedUp'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')])),
                ('payment_status', models.CharField(max_length=100, null=True, blank=True)),
                ('business', models.ForeignKey(to='haishin.Business')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=haishin.models.get_avatar_path, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
