# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import chargeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0005_auto_20151104_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='docfile',
            field=models.FileField(validators=[chargeapp.models.Upload.validate_file_extension, chargeapp.models.Upload.validate_file_size], upload_to='documents/'),
        ),
    ]
