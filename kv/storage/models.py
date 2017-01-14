from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Group(models.Model):
    key = models.CharField(max_length=128, null=False, blank=False, primary_key=True)
    last_modified = models.DateTimeField(default=now)
    password = models.CharField(max_length=128, null=True, blank=True, default='')


class Record(models.Model):
    group = models.ForeignKey('Group', null=False, blank=False)
    key = models.CharField(max_length=128, null=False, blank=False)
    value = models.TextField()
    last_modified = models.DateTimeField(default=now)
