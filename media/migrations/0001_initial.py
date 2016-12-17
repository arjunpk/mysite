# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 03:37
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
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('album_desc', models.CharField(blank=True, max_length=150)),
                ('share_to_fb', models.BooleanField()),
                ('has_photos', models.BooleanField()),
                ('total_media', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_title', models.CharField(blank=True, max_length=50)),
                ('photo_desc', models.CharField(blank=True, max_length=150)),
                ('original_image', models.CharField(blank=True, max_length=100)),
                ('display_image', models.CharField(max_length=100)),
                ('thumb_image', models.CharField(max_length=100)),
                ('share_to_fb', models.BooleanField()),
                ('share_to_tw', models.BooleanField()),
                ('share_to_ig', models.BooleanField()),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Albums')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(blank=True, max_length=50)),
                ('video_desc', models.CharField(blank=True, max_length=150)),
                ('original_video', models.CharField(blank=True, max_length=100)),
                ('display_video', models.CharField(max_length=100)),
                ('thumb_video', models.CharField(max_length=100)),
                ('share_to_fb', models.BooleanField()),
                ('share_to_tw', models.BooleanField()),
                ('share_to_ig', models.BooleanField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Albums')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]