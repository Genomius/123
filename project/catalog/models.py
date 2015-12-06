# coding: utf-8
from django.db import models


class Product(models.Model):
    referrer = models.CharField(u'Ссылка на магазин', max_length=1024)
    name = models.CharField(u'Имя', max_length=128)
    type = models.CharField(u'Тип', max_length=128)
    price = models.IntegerField(u'Цена')
    marking = models.CharField(u'Артикуль', max_length=128)
    description = models.TextField(u'Описание', max_length=1024)
    # size = models.CharField(u'Размер', max_length=16)
    # count = models.IntegerField(u'Количество')
    slug = models.SlugField(u'URL', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товар"