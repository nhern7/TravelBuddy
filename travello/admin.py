from django.contrib import admin
from .models import Destination, Guide

# Register your models here.

admin.site.register(Destination)  #allows superusers to create models of type Destination
admin.site.register(Guide) 