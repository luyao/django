#-*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User, check_password
from django.forms.fields  import EmailField, CharField, BooleanField
from django.forms.widgets import TextInput, PasswordInput, CheckboxInput, Textarea

from ssuser.models import RegistrationProfile
from adminTest import settings 

attrs_dict = {'class':'formitem'}

class RegistrationForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs=attrs_dict),
		error_messages={"invalid":"输入有效的邮箱地址吧",
		"required":"输入邮箱地址吧"})

	username = forms.CharField(widget=forms.TextInput(attrs=attrs_dict),
		max_length=10,
		error_messages={"required":"输入昵称吧",
		"max_length":"请限制在10个字符内"})

	password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict),
		max_length=16, min_length=6,
		error_messages={"required":"不能忘了密码",
		"max_length":"请限制在6到16个字符",
		"min_length":"请限制在6到16个字符"})

	password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict),
		error_messages={"required":"未确认密码"})

	tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
		initial=True, required=False)
	
	def clean_email(self):
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError("邮箱地址已被使用")
		return self.cleaned_data['email']
	
	def clean_username(self):
		#用户名不存在，则成功
		#用户名已被注册，失败
		#用户名是保留字，失败
		import re
		name_re = re.compile(u"^[-_.a-zA-Z01-9\u4e00-\u9fff]{1,10}$")
		if not re.match(name_re, self.cleaned_data['username']):
			raise forms.ValidationError("请使用中文、字母、数字、下划线、连字符或点.")

		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']

		raise forms.ValidationError("昵称已被使用")

	def clean_tos(self):
		if not self.cleaned_data.get('tos', True):
			raise forms.ValidationError("请同意并勾选用户协议")
		return self.cleaned_data['tos']

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				msg = "密码输入不一致，重新来吧"
				self._errors["password2"] = self.error_class([msg])
				del self.cleaned_data["password1"]
				del self.cleaned_data["password2"]

		return self.cleaned_data

	def save(self, profile_callback=None):
		new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
			password=self.cleaned_data['password1'],
			email=self.cleaned_data['email'],
			profile_callback=profile_callback)
		return new_user

class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(),
		error_messages={"invalid":"输入有效的邮箱地址吧",
		"required":"输入邮箱地址吧"})

	password = forms.CharField(widget=forms.PasswordInput(),
		error_messages={"required":"不能忘了密码"})

	def clean_email(self):
		try:
			user = User.objects.get(email=self.cleaned_data['email'])
		except User.DoesNotExist:
			raise forms.ValidationError("邮箱地址未注册")
		return self.cleaned_data['email']

	def clean(self):
		if "email" in self.cleaned_data and "password" in self.cleaned_data:
			user = User.objects.get(email__iexact=self.cleaned_data['email'])
			pw = self.cleaned_data["password"]
			if not check_password(pw, user.password):
				msg = "邮箱或密码不正确，请检查"
				self._errors["password"] = self.error_class([msg])
				del self.cleaned_data["password"]

		return self.cleaned_data

	def get_user(self):
		user = User.objects.get(email__iexact=self.cleaned_data['email'])
		return user

class IntroForm(forms.Form):
	intro = forms.CharField(widget=forms.Textarea, required=True)

class LogoForm(forms.Form):
	logo = forms.ImageField(required=True)
