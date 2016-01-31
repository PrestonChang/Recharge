# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0007_auto_20151117_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
