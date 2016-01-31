# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0006_auto_20151115_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lat',
            field=models.DecimalField(max_digits=20, decimal_places=15),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lon',
            field=models.DecimalField(max_digits=20, decimal_places=15),
        ),
        migrations.AlterUniqueTogether(
            name='chargingstation',
            unique_together=set([('lat', 'lon')]),
        ),
    ]
