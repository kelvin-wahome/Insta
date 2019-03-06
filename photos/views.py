# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Location,Category,Images
# Create your views here.

def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    images = Image.retrieve_all()
    return render (request, 'index.html',{'location':locations , 'categories':categories, 'images':images})
