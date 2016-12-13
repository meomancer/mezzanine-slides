# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('caption', models.CharField(max_length=200, verbose_name='Caption', blank=True)),
                ('page', models.ForeignKey(to='pages.Page')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ['_order'],
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]
