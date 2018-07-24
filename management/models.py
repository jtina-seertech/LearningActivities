# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Assets(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    asset_type = models.CharField(max_length=100, blank=True, default='')

class Status(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

class AssetsBorrower(models.Model):
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

