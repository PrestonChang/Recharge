# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0016_auto_20151125_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 23, 22, 10, 867516, tzinfo=utc)),
        ),
    ]
