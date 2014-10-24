# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure_hunt', '0002_auto_20141020_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(upload_to=b'levels'),
        ),
    ]
