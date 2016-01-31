# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0003_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='docfile',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
