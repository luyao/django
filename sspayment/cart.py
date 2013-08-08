#coding=utf8
#!/bin/python
# Program:
# 		
# History:
# Author: luyao(yaolu1103@gmail.com)
# Date:  2013/06/29 16:45:29

from adminTest.sspayment.models import LineItem

class Cart(object):
	def __init__(self, *args, **kwargs):
		self.items = []
		self.total_price = 0
	def add_product(self, product):
		self.total_price += product.price
		for item in self.items:
			if item.product.id == product.id: #merge same product
				item.quantity += 1
				return
		self.items.append(LineItem(product=product, unit_price=product.price, quantity=1))

	def __get_product_idx(self, product):
		idx = 0
		for item in self.items:
			if item.product.id == product.id: #find
				return idx
			++idx
		return -1

	#brief delete the product
	def del_product(self, product):
		idx = __get_product_idx(self, product)
		if idx != -1:
			item = self.items[idx]
			if item.quantity >= 1:
				self.total_price -= item.unit_price * item.quantity
				self.items.pop(idx)

	def del_one_product(self, product):
		idx = __get_product_idx(self, product)
		if idx != -1:
			item = self.items[idx]
			if items.quantity >= 1:
				self.total_price -= item.unit_price
				item.quantity -= 1



