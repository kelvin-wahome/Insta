# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length = 60)
    def save_image(self):
        self.save()


    def __str__(self):
        return self.category_name

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

    @classmethod
    def search_by_category(cls,search_term):
        result_search = cls.objects.filter(category__category_name__icontains=search_term)
        return result_search

    @classmethod
    def filter_by_location(cls,location):
        filter_by_location = cls.objects.filter_by(location__location_name__icontains=location)
        return filter_by_location

    @classmethod
    def get_image_by_id(cls,input_id):
        get_image_by_id = cls.objects.get(id=input_id)
        return get_image_by_id

    
