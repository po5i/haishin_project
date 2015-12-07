# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import haishin.models
import ckeditor.fields
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
                ('logo', models.ImageField(null=True, upload_to=haishin.models.get_logo_path, blank=True)),
                ('cover_image', models.ImageField(null=True, upload_to=haishin.models.get_business_cover_path, blank=True)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100, null=True, blank=True)),
                ('longitude', models.CharField(max_length=100, null=True, blank=True)),
                ('phone', models.CharField(max_length=100, null=True, blank=True)),
                ('discount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('average_time', models.IntegerField(default=0)),
                ('price_range', models.IntegerField(default=0)),
                ('published', models.BooleanField(default=True)),
                ('closed', models.BooleanField(default=False)),
                ('monday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('monday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('tuesday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('tuesday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('wednesday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('wednesday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('thursday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('thursday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('friday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('friday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('saturday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('saturday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('sunday_opens', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('sunday_closes', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
        ),
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'business categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(help_text=b'Ej: SCL, CABA, ...', max_length=5)),
                ('image', models.ImageField(null=True, upload_to=haishin.models.get_city_path, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(help_text=b'Ej: CL, AR, ...', max_length=3)),
                ('tax', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('shipping', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('average_delivery_time', models.IntegerField(default=30, help_text=b'En minutos', null=True, blank=True)),
                ('privacy', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('terms_conditions', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('about', ckeditor.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tags', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('published', models.BooleanField(default=True)),
                ('available_from', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('available_to', models.TimeField(help_text=b'America/Argentina/Buenos_Aires', null=True, blank=True)),
                ('business', models.ForeignKey(to='haishin.Business')),
            ],
            options={
                'verbose_name_plural': 'dishes',
            },
        ),
        migrations.CreateModel(
            name='DishAddon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
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
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'dish categories',
            },
        ),
        migrations.CreateModel(
            name='DishCustomization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('options', models.TextField(help_text=b'Opciones separadas con coma', null=True, blank=True)),
                ('dish', models.ForeignKey(to='haishin.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('swift_job_id', models.CharField(max_length=512, null=True, blank=True)),
                ('shippify_task_id', models.CharField(max_length=512, null=True, blank=True)),
                ('shippify_distance', models.FloatField(null=True, blank=True)),
                ('shippify_price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('payment_reference_id', models.CharField(max_length=512, null=True, blank=True)),
                ('recipient_name', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_address', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_phone', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_latitude', models.CharField(max_length=100, null=True, blank=True)),
                ('recipient_longitude', models.CharField(max_length=100, null=True, blank=True)),
                ('main_status', models.CharField(max_length=100, choices=[(b'Draft', b'Draft'), (b'Received', b'Received'), (b'Accepted', b'Accepted'), (b'Rejected', b'Rejected'), (b'Shipped', b'Shipped'), (b'Completed', b'Completed'), (b'Cancelled', b'Cancelled')])),
                ('delivery_date', models.DateTimeField(null=True, blank=True)),
                ('delivery_status', models.CharField(max_length=100, choices=[(b'1', b'Getting ready'), (b'2', b'Pending to assign'), (b'3', b'Pending for shipper response'), (b'4', b'Shipper confirmed'), (b'5', b'Being picked up'), (b'6', b'Being delivered'), (b'7', b'Delivered successfully'), (b'0', b'Cancelled')])),
                ('payment_status', models.CharField(max_length=100, null=True, blank=True)),
                ('remarks', models.TextField(null=True, blank=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('business', models.ForeignKey(to='haishin.Business')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('dish', models.ForeignKey(to='haishin.Dish')),
                ('job', models.ForeignKey(to='haishin.Job')),
            ],
        ),
        migrations.CreateModel(
            name='JobDetailAddon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('addon', models.ForeignKey(to='haishin.DishAddon')),
                ('job_detail', models.ForeignKey(related_name='addons', to='haishin.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='JobStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_status', models.CharField(max_length=100)),
                ('delivery_status', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(to='haishin.Job')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
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
                ('job', models.ForeignKey(to='haishin.Job')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=haishin.models.get_avatar_path, blank=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True, blank=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True, choices=[(b'braintree', b'braintree'), (b'stripe', b'stripe'), (b'manual', b'manual')])),
                ('city', models.ForeignKey(blank=True, to='haishin.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='haishin.Country', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('city', models.ForeignKey(to='haishin.City')),
            ],
            options={
                'ordering': ['city__country__name', 'city__name', 'name'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.ForeignKey(blank=True, to='haishin.Town', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dishaddon',
            name='category',
            field=models.ForeignKey(to='haishin.DishAddonCategory'),
        ),
        migrations.AddField(
            model_name='dishaddon',
            name='dish',
            field=models.ForeignKey(related_name='addons', to='haishin.Dish'),
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(to='haishin.DishCategory'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='haishin.Country'),
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(to='haishin.BusinessCategory'),
        ),
        migrations.AddField(
            model_name='business',
            name='town',
            field=models.ForeignKey(to='haishin.Town'),
        ),
    ]
