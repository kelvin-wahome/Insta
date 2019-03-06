# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Location,Category,Images
# Create your views here.

def index(request):
    '''
    Function that renders the index page
    '''

    photos = Image.get_all_images()
    return render (request, 'index.html',{"photos":photos})

def search_image(request):
    '''
    function to render search result
    '''
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})
    else:
        message = ".You haven't searched for any category"
        return render(request, 'search.html',{"message":message})
