# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 21:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.PositiveSmallIntegerField(choices=[(1, 'Photo'), (2, 'Video')], verbose_name='Media Type')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(blank=True, max_length=150)),
                ('orig_extension', models.CharField(max_length=5)),
                ('original_media_file', models.CharField(blank=True, max_length=100)),
                ('display_media_file', models.CharField(max_length=100)),
                ('thumb_media_file', models.CharField(max_length=100)),
                ('share_to_fb', models.BooleanField()),
                ('share_to_tw', models.BooleanField()),
                ('share_to_ig', models.BooleanField()),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media_alt_Res',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.PositiveSmallIntegerField(choices=[(1, '480p'), (2, '720p'), (3, '1080p')], verbose_name='Resolution')),
                ('media_file', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Media_Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=1000)),
                ('action_taken', models.BooleanField()),
                ('action_desc', models.CharField(max_length=1000)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('action_taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Action_Taken_By', to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Media')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reported_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='photos',
            name='album',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='album',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='user',
        ),
        migrations.AddField(
            model_name='albums',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
        migrations.AddField(
            model_name='media',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Albums'),
        ),
        migrations.AddField(
            model_name='media',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
