# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0017_auto_20160201_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 23, 22, 35, 674727, tzinfo=utc)),
        ),
    ]
