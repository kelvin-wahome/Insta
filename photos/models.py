# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Images(models.Model):

    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'articles/')
