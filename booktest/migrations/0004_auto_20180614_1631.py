# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_remove_bookinfo_isdelete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'ordering': ['-bpub_date']},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
