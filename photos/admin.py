# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Images,Category,Location

# Register your models here.
admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Location)
