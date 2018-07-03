# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class datatable1(models.Model):
    food = models.IntegerField()
    trip = models.IntegerField()
    shopping = models.IntegerField()
