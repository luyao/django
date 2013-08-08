#-*- coding:utf-8 -*-

from django.contrib import admin
from adminTest.ssuser.models import RegistrationProfile

class RegistrationProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'id','activated', 'activation_key', 'logoori', 'reputation', 'energy', 'level', 'score', 'logo')

admin.site.register(RegistrationProfile, RegistrationProfileAdmin)
