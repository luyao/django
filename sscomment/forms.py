#-*- coding:utf-8 -*-
#import time
#import datetime

from django import forms
import Image
import StringIO

#from django.conf import settings
#from django.forms.util import ErrorDict
#from django.utils.encoding import force_unicode
#from django.utils.translation import ungettext, ugettext_lazy as _
#from django.contrib.comments.forms import CommentSecurityForm
#from django.contrib.contenttypes.models import ContentType

from adminTest.sscomment.models import Qcomment
		
#attrs_dict = {'class':'formitem'}
class QcommentForm(forms.Form):
	#content = forms.CharField(widget=forms.Textarea, error_messages={'required':'空评论？'})
	content  = forms.CharField(required=False)
	absorption = forms.IntegerField(required=False)	
	durability = forms.IntegerField(required=False)	
	anti_blooming = forms.IntegerField(required=False)	
	ppr = forms.IntegerField(required=False)	
	color = forms.IntegerField(required=False)	

	#TODO 评论敏感词、脏话过滤
	#def clean_content(self):
	#	c = self.cleaned_data.get('content', '')
	#	c = c.strip()
	#	n= len(c)
	#	if n < 4:
	#		raise forms.ValidationError("评论过短，加几个字吧~~")
	#	return c
	#def clean_content(self):
	#	return self.cleaned_data.get('content', '')
	#def GetImg(self, request):
	#	file = request.FILES.get('file', None)
	#	if file:
	#		data = file['content']
	#		f = StringIO.StringIO(data)
	#		self.imgs = Image.open(f)
	#		return self.imgs
	#
	def GetComment(self):
		form = Qcomment()
		form.content       = self.cleaned_data.get('content', '')
		form.absorption    = self.cleaned_data.get('absorption', 0)
		form.durability    = self.cleaned_data.get('durability', 0)
		form.anti_blooming = self.cleaned_data.get('anti_blooming', 0)
		form.ppr           = self.cleaned_data.get('ppr', 0)
		form.color         = self.cleaned_data.get('color', 0)
		#form.imgs          = self.GetImg(request)
		return form

