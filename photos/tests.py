# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    '''
    Tests Location class and its functions and methods
    '''
    #Set up method
    def setUp(self):
        self.location = Location(name='Spain')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        '''
        Function to test that location is being saved
        '''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a location can be deleted
        '''
        self.location.save_location()
        self.location.delete_location()
