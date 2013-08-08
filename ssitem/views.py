# Create your views here.
#-*- coding:utf-8 -*-

from django.http 	import Http404, HttpResponse, HttpResponseRedirect
from django.template 	import RequestContext
from django.shortcuts 	import render_to_response, get_object_or_404
from django.db.models 	import Q
from django.contrib.auth.decorators 	import login_required
from django.contrib.contenttypes.models import ContentType

from sscomment.models 	import Qcomment
from ssitem.models 	import Shise
from sscomment.forms 	import QcommentForm

def shiseview(request, sid, form_class=QcommentForm, template_name="shise/jqq_shise.html"):
	shise = get_object_or_404(Shise, id=sid)


	qcommentall   = shise.qcomments.all()
	qcommentcount = qcommentall.count()
	qcommentall  = qcommentall[:5]
	if request.method == 'POST':
		if request.is_ajax():
			#处理申请试色请求
			action = request.POST.get('action', False)
			if action == 'shise':
				shise.checkiners.add(request.user)
				shise.checkin += 1
				shise.save()
				message = u"申请 %s 成功！" %shesi.name
			return HttpResponse(message)

		else:
			#处理添加评论请求
			form = form_class(request.POST)
			if form.is_valid():
				content = form.cleaned_data["content"]
				qcom = Qcomment(comment=content, has_quote=False, is_public=True, lights=0)
				qcom.author = request.user
				qcom.content_object = shise
				qcomlist = Qcomment.objects.filter(shise=shise, author=request.user)
				for oldqcom in qcomlist:
					if qcom.comment == oldqcom.comment:
						qcom = oldqcom
						successurl = '%s#qcomment-area' %(shise.get_absolute_url())
						return HttpResponseRedirect(successurl)
				qcom.save()
				successurl = '%s#qcomment-area' %(shise.get_absolute_url())
				return HttpResponseRedirect(successurl)
	else:
		form = form_class()

	context = RequestContext(request)
	return render_to_response(template_name, 
		{'shise':shise,
		'form':form, 'qcommentlist':qcommentall, 'qcommentcount':qcommentcount},
		context_instance=context)
