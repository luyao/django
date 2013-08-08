#coding=utf8
#!/bin/python
# Program:
# 		
# History:
# Author: luyao(yaolu1103@gmail.com)
# Date:  2013/06/28 15:05:47

from django.http import HttpResponse, Http404
import datetime
from django.template import Context, RequestContext

from django.template.loader import get_template
from django.shortcuts import render_to_response


from adminTest.homepageItem.models import homepageItem
from adminTest.homepageItem.models import homepageCate
from adminTest.ssitem.models import Shise

import Image
import StringIO
from datetime import datetime


def hello(request):
	t = get_template('scrollable/flux.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def addFile(request):
	if 0 and request.method == 'POST':
		file_obj = request.FILES.get('file', None)   
		if file_obj:
			data = file_obj['content']
			f = StringIO.StringIO(data)
			image = Image.open(f)
			image = image.convert('RGB')
			abs_name = '%s_%s_%s' %(str(request.user),\
					str(datetime.today()).replace(':', '-')[:-7],\
					file_obj['filename'])
		image.save(file(abs_name, 'wb'))
	t = get_template('form.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def underConstruct(request):
	t = get_template('underConstruct.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def hour_ahead(request, time):
	try:
		ahead = int(time)
	except ValueError:
		raise Http404()
	sDay = datetime.datetime.now() + datetime.timedelta(hours=ahead)
	t = get_template( 'time/time.html' )
	html = t.render( Context({'ahead':ahead, 'future_time':sDay}) )
	return HttpResponse(html)

def hour_ahead_ex(request, time):
	try:
		ahead = int(time)
	except ValueError:
		raise Http404()
	future_time = datetime.datetime.now() + datetime.timedelta(hours=ahead)
	return render_to_response('time/time.html', locals() )

def new_homepage(request):
	t = get_template('home/new_homepage.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def scroll_demo(request):
	t = get_template('scrollable/scroll_demo.html')
	item_stick = homepageItem.objects.all()[0:4]
	item_list = homepageItem.objects.all()
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def __initHomepageItem():
	test_cate = homepageCate.objects.create(
			title = 'test_cate',
			page  = 'http://122.200.77.77:1105/hello/',
			)

	for i in range(1,6):
		item = homepageItem.objects.create(
				title       = 'let us try some long title, to check if we can get the suitable margin',
				description = 'django test description, we need it to be very long to find the differece we need it to be very long to find the differece we need it to be very long to find the differece',
				image_url   = 'http://122.200.77.77:1107/static/img/%d.png' %(i),
				page_url    = 'http://122.200.77.77:1107/hello/',
				cate        = test_cate,
				price       = 200,
				);
		item.save()


def home_index(request):
	item_stick = Shise.objects.all()[0:4]
	item_list  = Shise.objects.all()[0:24]

	#make waterflow head part
	item_list_template = '<!--item list~-->\
			<div class="content_home" ><!--begin content-->\
			<!--begin loops-->\
			<div class="posts-loop container_12 clearfix masonry" style="position: relative;">'
	#make the waterflow item list
	top_offset = [0, 0, 0, 0]
	item_list = Shise.objects.all()
	i = 0
	item = item_list[0]
	for item in item_list:
		top_px  = 0
		index = i%4
		if (i >3 ):
			top_px  = top_offset[index]
		left_px = index*240
		t = get_template('home/item_list.html')
		c = RequestContext(request, locals())
		f = len(item.description) / 30.0
		top_offset[index] += 275  # the image, margin and the title height
		top_offset[index] += 39 * int(round(f))
		if top_offset[index] >= 25000:
			end_id = item.id        #watermark, uesd to next round
			break
		item_list_template += t.render(c)
		i += 1

	end_id = item.id
	item_list_template += "<div id='watermark' title='%s' style='height:'%d px''></div></div><!--end loops--></div>" %(end_id,top_offset[0]+30)

	offset = 2500
	if (top_offset[0]):
		offset = top_offset[0] + 1000
	return render_to_response("home/index.html", 
				{
					'item_list_template':item_list_template,
					'item_stick':item_stick,
					'top_offset':offset,
				}
			)



def post_item(request, id):
	return Http404()


