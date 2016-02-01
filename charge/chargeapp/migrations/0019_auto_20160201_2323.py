# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0018_auto_20160201_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='next_available',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 23, 23, 46, 655070, tzinfo=utc)),
        ),
    ]
