#coding=utf8
#!/bin/python
# Program:
# 		
# History:
# Author: luyao(yaolu1103@gmail.com)
# Date:  2013/06/29 16:43:31

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.template.loader import get_template
#from django.shortcuts import render_to_response

from cart import Cart
from adminTest.sspayment.models import Product, LineItem

def __get_cart(request):
	cart = request.session.get("cart", None)
	if not cart:
		cart = Cart()
		request.session["cart"] = cart
	return cart

def cart_view(request):
	#define cart is used for using locals
	cart = __get_cart(request)
	t = get_template('cart/cart.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def _get_method_pointer(class_obj, method_name):
	mtd = getattr(class_obj, method_name)
	return mtd # call def

def _oper_framework(request, id, function):
	product = Product.objects.get(id = id)
	cart = __get_cart(request)
	_get_method_pointer(cart, function)(product)
	#update the cart in the session
	request.session["cart"] = cart
	return cart_view(request)

def add_to_cart(request, id):
	"""
	product = Product.objects.get(id = id)
	cart = __get_cart(request)
	cart.add_product(product)
	#update the cart in the session
	request.session["cart"] = cart
	return cart_view(request)
	"""
	return _oper_framework(request, id, "add_product")

def del_from_cart(request, id):
	cart = __get_cart(request)
	product = Product.objects.get(id = id)
	cart.del_product(product)
	request.session["cart"] = cart
	return cart_view(request)

def clean_cart(request):
	request.session["cart"] = Cart()
	return cart_view(request)


def pay(request):
	raise Http404()
