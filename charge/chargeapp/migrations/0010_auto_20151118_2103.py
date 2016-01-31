# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0009_auto_20151118_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adminDataOnly',
            new_name='admin_data_only',
        ),
    ]
