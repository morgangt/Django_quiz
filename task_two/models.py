from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Type_Action(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title.encode('ascii', errors='replace')


class Action_User(models.Model):
    type_action = models.ForeignKey(Type_Action)
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    class Meta:
        unique_together = ('type_action', 'user', 'date',)
