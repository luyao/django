#-*- coding:utf-8 -*-
from django.db import models
from django.db.models import signals
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

from adminTest.sscomment.models import Qcomment
from adminTest.settings import MEDIA_ROOT
from adminTest.common import shiselogo, generate_shiselogoori_name

import os
import uuid
import datetime

#一个试色彩妆品
class Shise(models.Model):
	#妆品信息
	name 		= models.CharField(max_length=60, verbose_name='彩妆名')
	brand 		= models.CharField(max_length=60, verbose_name='品牌', blank=True)
	spec 		= models.CharField(max_length=60, verbose_name='规格', blank=True)
	category	= models.CharField(max_length=60, verbose_name='分类', blank=True)
	barcode		= models.CharField(max_length=60, verbose_name='条形码', blank=True)
	function	= models.CharField(max_length=60, verbose_name='功效', blank=True)
	composition	= models.CharField(max_length=60, verbose_name='成分', blank=True)
	description	= models.CharField(max_length=300, verbose_name='描述', blank=True)
	remark 		= models.CharField(max_length=100, verbose_name='补充说明', blank=True)

	logoori 	= models.ImageField('logo原图',	upload_to=generate_shiselogoori_name, 	blank=True)
	logo300 	= models.ImageField('logo大图',	upload_to='shiselogo', 	blank=True)
	logo110 	= models.ImageField('logo小图',	upload_to='shiselogo', 	blank=True)

	#创建者
	author 		= models.ForeignKey(User, related_name='shise_author_set', verbose_name='创建者')
	#评论
	qcomments 	= generic.GenericRelation(Qcomment)

	like 		= models.IntegerField('喜欢数', default=0, editable=False)
	likers		= models.ManyToManyField(User, related_name='shise_likers_set', verbose_name='喜欢的人', blank=True, editable=False)
	checkin		= models.IntegerField('申请数', default=0, editable=False)
	checkiners	= models.ManyToManyField(User, related_name='shise_checkiners_set',  verbose_name='申请试色的人', blank=True, editable=False)

	class Meta:
		verbose_name_plural = "Shises"
		ordering = ('-id', 'brand', )
		verbose_name = u"试色彩妆品"

	def __unicode__(self):
		return u'%s %s %s' %(self.name, self.brand, self.category)

	def get_name(self):
		return self.name

	def get_creator(self):
		return self.author

	def get_absolute_url(self):
		return u'/shise/%s/' % self.id

	def thumbnail(self):
		oribase, ext = os.path.splitext(os.path.basename(self.logoori.path))
		ext = ".jpg"

		#生成 300x300 logo大缩略图
		base = "300_%d_%s_%s" %(int(self.id), uuid.uuid4().hex[:8], oribase)
		t1 = shiselogo(os.path.join(MEDIA_ROOT, self.logoori.name), 300)
		t1_path = os.path.join(MEDIA_ROOT, 'shiselogo/' + base + ext)
		t1.save(t1_path, quality=100)
		self.logo300= ImageFieldFile(self, self.logo300, 'shiselogo/' + base + ext)

		#生成 110x110 logo小缩略图
		base = "110_%d_%s_%s" %(int(self.id), uuid.uuid4().hex[:8], oribase)
		t1 = shiselogo(os.path.join(MEDIA_ROOT, self.logoori.name), 110)
		t1_path = os.path.join(MEDIA_ROOT, 'shiselogo/' + base + ext)
		t1.save(t1_path, quality=100)
		self.logo110= ImageFieldFile(self, self.logo110, 'shiselogo/' + base + ext)

		self.save()

def thumbnail_shiseLogo(sender, instance, created, **kwargs):
	if created:
		if instance.logoori:
			instance.thumbnail()
	else:
		return

#save完成后发出此信号
signals.post_save.connect(thumbnail_shiseLogo, sender=Shise, dispatch_uid="ssitem.models.logo")
