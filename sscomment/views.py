#-*- coding:utf-8 -*-

from django import http
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import escape
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

from adminTest.sscomment.models import Qcomment

class CommentPostBadRequest(http.HttpResponseBadRequest):
    def __init__(self, why):
        super(CommentPostBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("comments/400-debug.html", {"why": why})

@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):
	data = request.POST.copy()
	if request.user.is_authenticated():
		data["name"] = request.user.username

	next = data.get("next", next)

	# Look up the object we're trying to comment about
	#貌似这些检查都没什么用。先保留着吧
	ctype = data.get("content_type")
	object_pk = data.get("object_pk")
	if ctype is None or object_pk is None:
		return CommentPostBadRequest("Missing content_type or object_pk field.")
	try:
		model = models.get_model(*ctype.split(".", 1))
		target = model._default_manager.using(using).get(pk=object_pk)
	except TypeError:
		return CommentPostBadRequest("Invalid content_type value: %r" % escape(ctype))
	except AttributeError:
		return CommentPostBadRequest(
			"The given content-type %r does not resolve to a valid model." % escape(ctype))
	except ObjectDoesNotExist:
		return CommentPostBadRequest(
			"No object matching content-type %r and object PK %r exists." % \
			(escape(ctype), escape(object_pk)))
	except (ValueError, ValidationError), e:
		return CommentPostBadRequest(
			"Attempting go get content-type %r and object PK %r exists raised %s" % \
			(escape(ctype), escape(object_pk), e.__class__.__name__))

	# Construct the comment form
	form = sscomment.get_form()(target, data=data)

	# Check security information
	if form.security_errors():
		return CommentPostBadRequest(
			"The comment form failed security verification: %s" %escape(str(form.security_errors())))

	url = request.META[path]
	#若评论出现，不提示错误，跳转到本页面
	#if form.errors: 
	#	return HttpResponseRedirect(url)
	
	#发布评论成功，保存到数据库
	comment = form.get_comment_object()
	#comment.ip_address = request.META.get("REMOTE_ADDR", None)
	if request.user.is_authenticated():
		comment.user = request.user
	comment.save()
	return HttpResponseRedirect(url)
