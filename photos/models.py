# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Images(models.Model):

    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'articles/')
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

     def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.category_name
