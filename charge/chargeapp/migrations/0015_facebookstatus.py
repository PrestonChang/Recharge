# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chargeapp', '0014_auto_20151123_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved')], max_length=255, default='draft')),
                ('publish_timestamp', models.DateTimeField(null=True, blank=True)),
                ('message', models.TextField(max_length=255)),
                ('link', models.URLField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['publish_timestamp'],
                'verbose_name_plural': 'Facebook Statuses',
            },
        ),
    ]
