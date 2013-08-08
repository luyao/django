#-*- coding:utf-8 -*-
# Create your views here.
import urlparse

from django.conf              import settings
from django.core.urlresolvers import reverse
from django.http              import HttpResponseRedirect, HttpResponse
from django.shortcuts         import render_to_response, get_object_or_404
from django.template          import RequestContext
from django.contrib.auth      import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from ssuser.forms  import RegistrationForm, LoginForm, IntroForm, LogoForm
from ssuser.models import RegistrationProfile

from sscomment.models	import Qcomment
from sscomment.forms	import QcommentForm

#账号激活
#1. 成功激活：重定向至含激活成功信息的登陆页面
#2. 重复激活：重定向至含已激活信息的登陆页面
#3. 激活失败：重定向至含激活失败信息的注册页面
def activate(request, activation_key, template_name='registration/login.html', extra_context=None):
	activation_key = activation_key.lower() # Normalize before trying anything with it.

	try:
		profile = RegistrationProfile.objects.get(activation_key=activation_key)
	except RegistrationProfile.DoesNotExist:
		#key不存在，无对应profile，重定向至注册
		return HttpResponseRedirect("/accounts/aregister/")
	
	#key存在，尝试激活user
	user = RegistrationProfile.objects.activate_user(activation_key)
	
	if not user:
		#key过期，激活无效，重定向至注册
		return HttpResponseRedirect("/accounts/aregister/")
	
	#到这里，激活成功，不管是之前已激活过还是这次激活
	#下面这段代码来自网上，貌似没用。为了表示对作者的尊重，暂保留
	if extra_context is None:
		extra_context = {}

	context = RequestContext(request)
	for key, value in extra_context.items():
		context[key] = callable(value) and value() or value
	#重定向至激活成功、登陆页面
	return HttpResponseRedirect("/accounts/alogin/")

#用户注册
def register(request, success_url='/', form_class=RegistrationForm, profile_callback=None,
             template_name='registration/register.html', extra_context=None):
	#如果用户已登陆，输入注册url，你是闹着玩呢，重定向至主页
	if request.user.is_authenticated():
		return HttpResponseRedirect(success_url)
	else:
	#核心注册流程
	#这部分代码来自网上
		if request.method == 'POST':
			form = form_class(data=request.POST, files=request.FILES)
			if form.is_valid():
				new_user = form.save(profile_callback=profile_callback)
				email = form.cleaned_data['email']
				success_url = '/accounts/email/%s/' %email
				return HttpResponseRedirect(success_url)
		else:
			form = form_class()
		
		if extra_context is None:
			extra_context = {}
		context = RequestContext(request)
		for key, value in extra_context.items():
			context[key] = callable(value) and value() or value
		return render_to_response(template_name, {'form':form}, context_instance=context)

#查收确认信
def accemail(request, emailaddress):
	try:
		account = RegistrationProfile.objects.get(user__email=emailaddress)
	except RegistrationProfile.DoesNotExist:
		#无效的email地址
		return HttpResponseRedirect("/accounts/register/")

	#帐号已激活
	if account.user.is_active:
		return HttpResponseRedirect("/accounts/login/")

	return render_to_response("registration/accemail.html", {"emailaddress":emailaddress})

#邮箱登陆
#若已登陆，则重定向至主页
#若账号已创建但未激活，重定向至lregister重新注册
def emaillogin(request, form_class=LoginForm, redirect_field_name='next',
		template_name='registration/login.html'):
	redirect_to = request.REQUEST.get(redirect_field_name, '')

	if request.user.is_authenticated():
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	else:
		if request.method == 'POST':
			form = form_class(data=request.POST)
			if form.is_valid():
				netloc = urlparse.urlparse(redirect_to)[1]
				if not redirect_to:
					redirect_to = settings.LOGIN_REDIRECT_URL
				elif netloc and netloc != request.get_host():
					redirect_to = settings.LOGIN_REDIRECT_URL

				#LoginForm的clean规则保证了user一定有，否则is_valid()返回False
				user = form.get_user()
				username = user.username
				password = form.cleaned_data["password"]
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						return HttpResponseRedirect(redirect_to)
					else:
						return HttpResponseRedirect("/accounts/lregister/")
		else:
			form = form_class()

		context = RequestContext(request)
		return render_to_response(template_name,
				{'form':form, redirect_field_name:redirect_to,},
				context_instance=context)

#用户协议
def accagreement(request):
	context = RequestContext(request)
	return render_to_response("registration/agreement.html", context_instance=context)



#修改logo
@login_required
def userview_logonew(request, form_class=LogoForm, template_name='registration/jqq_user_logonew.html'):
	user = request.user
	profile = user.get_profile()

	if request.method == 'POST':
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			userlogo = form.cleaned_data["logo"]
			profile.logoori = userlogo
			profile.save()
			profile.thumbnail()

			successurl = profile.get_absolute_url()
			return HttpResponseRedirect(successurl)
	else:
		form = form_class()

	context = RequestContext(request)
	return render_to_response(template_name,
				{'form':form, 'profile':profile},
				context_instance=context)

def userview_comment(request, rpid, form_class=QcommentForm, template_name='registration/jqq_user_comment.html'):
	profile = get_object_or_404(RegistrationProfile, id=rpid)

	qcommentall   = profile.qcomments.all()
	#qcommentall   = profile.qcomments.all().order_by('-submit_date')
	qcommentcount = qcommentall.count()
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			content = form.cleaned_data["content"]
			qcom = Qcomment(comment=content,
					has_quote=False,
					is_public=True,
					lights=0,
					author=request.user,
					content_object=profile)
			qcom.save()
			
			#留言后生成消息通知，告知留言
			#若是自己留言，request.user == profile.user，则不提醒
			if profile.user != request.user:
				note = u'<a class="vi-link" target="_blank" href="%s">%s</a> 给你 <a class="vi-link" target="_blank" href="%s">留言</a> 了，去看看吧。' %(request.user.get_profile().get_absolute_url(),
				request.user.username,
				profile.get_comment_url())

				ntype = 11
				iqnote = Qnote(noter=request.user, noteeid=profile.id, note=note, ntype=ntype)
				iqnote.save()

			successurl = '%s' %(profile.get_comment_url())
			return HttpResponseRedirect(successurl)
	else:
		form = form_class()

	context = RequestContext(request)
	return render_to_response(template_name,
				{'profile':profile, 'form':form,
				'qcommentlist':qcommentall, 'qcommentcount':qcommentcount, 'allcomments_now':True},
				context_instance=context)
