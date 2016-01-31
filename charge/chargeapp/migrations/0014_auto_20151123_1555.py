# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0013_auto_20151118_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sidebar_colour',
            field=models.CharField(max_length=3, choices=[('BLK', 'black'), ('BLU', 'blue'), ('GRY', 'grey'), ('RED', 'red'), ('GRN', 'green')], default='BLK'),
        ),
    ]
