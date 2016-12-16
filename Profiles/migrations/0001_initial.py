# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 02:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Photographer'), (2, 'Service Provider')], verbose_name='user type')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('tag_line', models.TextField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='gender')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Photographer'), (2, 'Service Provider'), (3, 'Customer'), (4, 'Explore Mode')], verbose_name='user type')),
                ('start_price_range', models.IntegerField()),
                ('end_price_range', models.IntegerField()),
                ('fb_profile_connected', models.BooleanField()),
                ('fb_profile', models.CharField(blank=True, max_length=500)),
                ('fb_page_connected', models.BooleanField()),
                ('fb_page', models.CharField(blank=True, max_length=500)),
                ('tw_profile_connected', models.BooleanField()),
                ('tw_profile', models.CharField(blank=True, max_length=500)),
                ('ig_profile_connected', models.BooleanField()),
                ('ig_profile', models.CharField(blank=True, max_length=500)),
                ('email_confirmed', models.BooleanField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.Cities')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='ZipCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(blank=True, max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.Cities')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.Countries')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.States')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.Countries'),
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiles.States'),
        ),
    ]
