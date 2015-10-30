# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haishin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(help_text=b'Ej: SCL, BSAS, ...', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(help_text=b'Ej: CL, AR, ...', max_length=3)),
                ('tax', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish', models.ForeignKey(to='haishin.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='JobStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_status', models.CharField(max_length=100)),
                ('delivery_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('city', models.ForeignKey(to='haishin.City')),
                ('country', models.ForeignKey(to='haishin.Country')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='average_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business',
            name='discount',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='business',
            name='latitude',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='longitude',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='remarks',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'braintree', b'braintree'), (b'stripe', b'stripe'), (b'manual', b'manual')]),
        ),
        migrations.AlterField(
            model_name='business',
            name='city',
            field=models.ForeignKey(default=1, to='haishin.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='country',
            field=models.ForeignKey(default=1, to='haishin.Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, to='haishin.City', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(blank=True, to='haishin.Country', null=True),
        ),
        migrations.AddField(
            model_name='jobstatushistory',
            name='job',
            field=models.ForeignKey(to='haishin.Job'),
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='job',
            field=models.ForeignKey(to='haishin.Job'),
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(default=1, to='haishin.BusinessCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='town',
            field=models.ForeignKey(default=1, to='haishin.Town'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=1, to='haishin.BusinessCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.ForeignKey(blank=True, to='haishin.Town', null=True),
        ),
    ]
