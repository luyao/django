#coding=utf8
#!/bin/python
# Program:
# 		
# History:
# Author: luyao(yaolu1103@gmail.com)
# Date:  2013/06/29 16:43:31

from django.db import models


class Product(models.Model):
	title          = models.CharField(max_length=100)
	description    = models.TextField()
	image_url      = models.CharField(max_length=200)
	price          = models.DecimalField(max_digits=8,decimal_places=2)



# Create your models here.
class LineItem(models.Model):
	product = models.ForeignKey(Product)
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField()

