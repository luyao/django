#-*- coding:utf-8 -*-
import datetime
import re
#import sha
#import random
import hashlib
import os
from itertools import chain

from django.db 	 import models
from django.core.mail import EmailMessage
from django.template.loader 	import render_to_string
from django.utils.translation 	import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes import generic
from django.db.models.fields.files import ImageFieldFile

from django.conf import settings
from adminTest.common  import ssuserlogo, generate_userlogoori_name
from adminTest.settings 	   import MEDIA_ROOT
from adminTest.sscomment.models  import Qcomment

SHA1_RE = re.compile('^[a-f0-9]{32}$')


class RegistrationManager(models.Manager):
	def activate_user(self, activation_key):
		if SHA1_RE.search(activation_key):
			try:
				profile = self.get(activation_key=activation_key)
			except self.model.DoesNotExist:
				#没找到激活码对应的用户，返回False
				return False
			#已激活过，直接返回user
			if profile.activation_key_activated():
				user = profile.user
				return user
			#若key没过期，则现在来激活，并返回激活后的user
			#激活后，一个新用户诞生了。邮件通知管理员
			#TODO 各种邮件通知收件人写入配置文件
			if not profile.activation_key_expired():
				user = profile.user
				#用户设置为活跃
				user.is_active = True
				user.save()
				#用户状态设置为激活
				profile.activated = True
				profile.save()

				#邮件通知
				subject = u'%s，欢迎您加入试色' %user.username
				message = render_to_string('registration/newUser.txt', {'rp': profile})
				to = []
				to.append(user.email)
				#TODO 发件人
				mail = EmailMessage(subject, message, to=to, from_email=settings.DEFAULT_FROM_EMAIL)
				mail.send()

				#最后返回用户
				return user
		#其他未知错误，返回False
		return False

	def create_inactive_user(self, username, password, email, send_email=True, profile_callback=None):
		new_user = User.objects.create_user(username, email, password)
		new_user.is_active = False
		new_user.save()
		
		registration_profile = self.create_profile(new_user)
		
		if profile_callback is not None:
			profile_callback(user=new_user)
		
		#send_email 控制发送验证邮件
		if send_email:
			subject = render_to_string('registration/activation_email_subject.txt',
					{'site': settings.SITE_NAME})
			# Email subject *must not* contain newlines
			# 不知道下面这行是干嘛的，看起来很牛的样子
			subject = ''.join(subject.splitlines())
			message = render_to_string('registration/activation_email_zh.txt',
					{'activation_key': registration_profile.activation_key,
					'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
					'site_address': settings.SITE_ADDRESS,
					'site': settings.SITE_NAME})
		    
			mail = EmailMessage(subject, message, to=[new_user.email], from_email=settings.DEFAULT_FROM_EMAIL);
			mail.send()
		return new_user

	def create_profile(self, user):
		#salt = sha.new(str(random.random())).hexdigest()[:5]
		#不能使用用户名来生成sha值，因为貌似sha参数不能处理unicode(或具体点，中文？)，具体没调试
		#使用email生成激活码
		#activation_key = sha.new(salt+user.email).hexdigest()
		activation_key = hashlib.new("md5", user.email).hexdigest()

		#TODO 这里随机生成logo图片
		return self.create(user=user,
				logo=settings.DEFAULT_LOGO_PATH, 
				logobig=settings.DEFAULT_LOGO_PATH,
				logoori=settings.DEFAULT_LOGO_PATH,
				activation_key=activation_key,
				activated=False)

	#删除已过期未激活的帐号
	#慎用
	def delete_expired_users(self):
		for profile in self.all():
			if profile.activation_key_expired():
				user = profile.user
				if not user.is_active:
					user.delete()

#扩展的user类，RP，俗称“人品”
#目前添加了验证码、logo、自我介绍字段
#新增 reputation 威望值、energy 活力值
#logoori: 原图片 
#logobig: 专用于用户主页展示的大logo, 命令方式为home_xxx.jpg
#logo:    50x50的小logo，默认的logo, 命名方式为50_xxx.jpg 
#用户未上传图片时，使用默认的logobig和logo
class RegistrationProfile(models.Model):
	user 		= models.ForeignKey(User, unique=True, verbose_name="用户")
	logo 		= models.ImageField('小logo50', upload_to='userlogo', blank=True)
	logobig		= models.ImageField('大logo',   upload_to='userlogo', blank=True)
	logoori 	= models.ImageField('logo原图', upload_to=generate_userlogoori_name, 	blank=True)
	reputation	= models.IntegerField('威望值', default=22)
	energy		= models.IntegerField('活力值', default=1024)
	level		= models.IntegerField('等级', 	default=1)
	score		= models.IntegerField('积分', 	default=1024)

	intro 		= models.TextField('自我介绍',  blank=True)
	activation_key  = models.CharField("激活码", max_length=40)
	activated 	= models.BooleanField("激活状态")


	qcomments 	= generic.GenericRelation(Qcomment)
	
	objects 	= RegistrationManager()

	def thumbnail(self):
		#生成用户页面较大图
		base, ext = os.path.splitext(os.path.basename(self.logoori.path))
		t1 = ssuserlogo(os.path.join(MEDIA_ROOT, self.logoori.name), 180, 1.3)
		t1_path = os.path.join(MEDIA_ROOT, 'userlogo/home_' + base + ext)
		t1.save(t1_path, quality=100)
		self.logobig = ImageFieldFile(self, self.logobig, 'userlogo/home_' + base + ext)

		#生成50x50小图
		t5 = ssuserlogo(os.path.join(MEDIA_ROOT, self.logoori.name), 50, 1.0)
		t5_path = os.path.join(MEDIA_ROOT, 'userlogo/50_' + base + ext)
		t5.save(t5_path, quality=100)
		self.logo = ImageFieldFile(self, self.logo, 'userlogo/50_' + base + ext)

		self.save()
	
	def __unicode__(self):
		return u"%s [reputation %d energy %d]" %(self.user, self.reputation, self.energy)
	
	#威望值处理
	def get_reputation(self):
		return self.reputation
	def set_reputation(self, n):
		self.reputation = n
	def add_reputation(self, n):
		self.reputation = self.reputation + n

	#活力值处理
	def get_energy(self):
		return self.energy
	def set_energy(self, n):
		self.energy = n
	def add_energy(self, n):
		self.energy = self.energy + n

	#积分处理
	def get_score(self):
		return self.score
	def set_score(self, n):
		self.score = n
	def add_score(self, n):
		self.score = self.score + n

	#等级处理
	def get_level(self):
		return self.level
	def set_level(self, n):
		self.level = n
	def add_level(self, n):
		self.level = self.level + n
	def activation_key_expired(self):
		expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
		return (self.user.date_joined + expiration_date <= datetime.datetime.now())
	activation_key_expired.boolean = True

	def activation_key_activated(self):
		return self.activated 
	activation_key_activated.boolean = True


	def get_uid(self):
		return self.user.id
	def get_rpid(self):
		return self.id

	def get_logo_url(self):
		return self.logo.url
	def get_absolute_url(self):
		return u'/accounts/%s/' %(self.id)
	def get_comment_url(self):
		return u'/accounts/%s/commentall/' %(self.id)
