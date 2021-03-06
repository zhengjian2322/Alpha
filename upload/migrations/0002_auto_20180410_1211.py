# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ques',
            name='imageA',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='ques',
            name='imageB',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='ques',
            name='imageC',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='ques',
            name='imageD',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='ques',
            name='question',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ques',
            name='voice',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
