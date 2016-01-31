# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0017_auto_20151125_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 11, 9, 54, 418128, tzinfo=utc)),
        ),
    ]
