# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='lat',
            field=models.DecimalField(max_digits=20, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lon',
            field=models.DecimalField(max_digits=20, decimal_places=10),
        ),
    ]
