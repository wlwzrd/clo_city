# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Commune',
                'verbose_name_plural': 'Communes',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Commune')),
            ],
            options={
                'verbose_name': 'Neighborhood',
                'verbose_name_plural': 'Neighborhoods',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
                ('address', models.CharField(default='Av 3N', max_length=200)),
                ('phone', models.CharField(default='1234567890', max_length=10)),
            ],
            options={
                'verbose_name': 'Commerce',
                'verbose_name_plural': 'Commerces',
            },
        ),
        migrations.CreateModel(
            name='SiteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SiteImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/sites/')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Site Image',
                'verbose_name_plural': 'Site Images',
            },
        ),
        migrations.AddField(
            model_name='site',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.SiteCategory'),
        ),
        migrations.AddField(
            model_name='site',
            name='neighborhood',
            field=models.ManyToManyField(to='sites.Neighborhood'),
        ),
    ]
