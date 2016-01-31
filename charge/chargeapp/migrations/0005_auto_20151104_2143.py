# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import chargeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('chargeapp', '0004_auto_20151104_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='docfile',
            field=models.FileField(validators=[chargeapp.models.Upload.validate_file_extension], upload_to='documents/'),
        ),
    ]
