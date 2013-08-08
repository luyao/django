#-*- coding:utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from adminTest.ssitem.models import Shise

class ShiseAdmin(admin.ModelAdmin):
	list_display = ('id', 'author', 'name', 'brand', 'spec', 'category', 'function')
	formfield_overrides = {
		models.CharField:{'widget':TextInput(attrs={'size':'150'})},
	}

admin.site.register(Shise, ShiseAdmin)
