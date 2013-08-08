#coding=utf8
#!/bin/python
# Program:
# 		
# History:
# Author: luyao(yaolu1103@gmail.com)
# Date:  2013/06/29 16:43:31

from django.db import models
from datetime import datetime 


#class Product(models.Model):
#	user           = models.ManyToManyField(User)
#class User(models.Model):
#	product        = models.ManyToManyField(Product);
#

class homepageCate(models.Model):
	title          = models.CharField(max_length=100)
	page           = models.URLField()


class homepageItem(models.Model):
	#owner          = models.ManyToManyField(User)
	#product        = models.ForeignKey(Product)
	title          = models.CharField(max_length=100)#title
	date           = models.DateField(default=datetime.now )              #insert time
	description    = models.TextField()              #the item information in detail
	image_url      = models.URLField()               #the image link for the item
	page_url       = models.URLField()               #the introduce link for the item
	cate           = models.ForeignKey(homepageCate) #the cate for the item
	price          = models.DecimalField(max_digits=8,decimal_places=2)


