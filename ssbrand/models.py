#-*- coding:utf-8 -*-
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from adminTest.common import generate_shiselogoori_name

# Create your models here.
class Brand(models.Model):
	name 		= models.CharField(max_length=60, verbose_name='彩妆名')
	logo 	    = models.ImageField('logo原图',	upload_to=generate_shiselogoori_name, 	blank=True)

	def __unicode__(self):
		return self.name

