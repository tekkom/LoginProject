# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Event(models.Model):
    title      = models.CharField(max_length=128, unique=True)
    logo       = models.FileField(blank=True, null=True)
    image      = models.FileField(blank=True, null=True)
    body       = models.TextField()
    created_at = models.DateField(db_index=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=False)
