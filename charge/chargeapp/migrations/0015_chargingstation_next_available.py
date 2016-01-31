# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0014_auto_20151119_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 23, 11, 46, 49231, tzinfo=utc)),
        ),
    ]
