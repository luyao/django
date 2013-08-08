#-*- coding:utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from adminTest.ssbrand.models import Brand
class BrandAdmin(admin.ModelAdmin):
	list_display = ('id',  'name')
	formfield_overrides = {
		models.CharField:{'widget':TextInput(attrs={'size':'150'})},
	}

admin.site.register(Brand, BrandAdmin)
