# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='referrer',
            field=models.CharField(default=1, max_length=1024, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043c\u0430\u0433\u0430\u0437\u0438\u043d'),
            preserve_default=False,
        ),
    ]
