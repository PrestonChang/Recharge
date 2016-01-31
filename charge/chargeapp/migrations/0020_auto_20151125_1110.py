# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0019_auto_20151125_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 11, 10, 0, 793317, tzinfo=utc)),
        ),
    ]
