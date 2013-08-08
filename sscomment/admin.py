#-*- coding:utf-8 -*-

from django.contrib import admin
from adminTest.sscomment.models import Qcomment

class QcommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'content_type', 'object_id', 'submit_date', 'author', 'content', 'has_quote', 'quote', 'lights', 'is_public')

admin.site.register(Qcomment, QcommentAdmin)
