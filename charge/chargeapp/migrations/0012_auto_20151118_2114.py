# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0011_auto_20151118_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sidebar_colour',
            field=models.CharField(choices=[('BLK', 'black'), ('BLU', 'blue'), ('PNK', 'pink'), ('RED', 'red'), ('GRN', 'green')], default='BLU', max_length=3),
        ),
    ]
