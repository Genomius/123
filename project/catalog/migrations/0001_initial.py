# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('type', models.CharField(max_length=128, verbose_name='\u0422\u0438\u043f')),
                ('price', models.IntegerField(verbose_name='\u0426\u0435\u043d\u0430')),
                ('marking', models.CharField(max_length=128, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b\u044c')),
                ('description', models.TextField(max_length=1024, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('size', models.CharField(max_length=16, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440')),
                ('count', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440',
            },
        ),
    ]
