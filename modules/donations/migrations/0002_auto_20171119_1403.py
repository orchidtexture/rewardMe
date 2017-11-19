# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-19 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.Category'),
        ),
        migrations.AddField(
            model_name='donation',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Goal'),
        ),
        migrations.AddField(
            model_name='donation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
