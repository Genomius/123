# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_referrer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f'),
        ),
    ]
