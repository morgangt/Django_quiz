# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

TRANSPORT_CAT = (
    ("A", u"Мотоцикл"),
    ("B", u"Автомобиль"),
    ("C", u"Грузовик"),
    ("D", u"Автобус"),
    ("BE", u"Автомобиль с прицепом"),
    ("CE", u"Грузовик с прицепом"),
    ("DE", u"Автобус с прицепом"),
)


class Transportation(models.Model):
    to_date = models.DateTimeField(default=timezone.now)
    model = models.CharField(max_length=200)
    cat = models.CharField(max_length=2, choices=TRANSPORT_CAT, default='B')

    def __str__(self):
        return self.model
