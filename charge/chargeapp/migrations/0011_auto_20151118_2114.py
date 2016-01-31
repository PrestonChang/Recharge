# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0010_auto_20151118_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sidebar_colour',
            field=models.CharField(max_length=3, choices=[('BLK', 'black'), ('BLU', 'blue'), ('PNK', 'pink'), ('RED', 'red'), ('GRN', 'green')], default='BLK'),
        ),
    ]
