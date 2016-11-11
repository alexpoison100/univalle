# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20161110_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripciones',
            name='id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
