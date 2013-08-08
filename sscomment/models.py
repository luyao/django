#-*- coding:utf-8 -*-

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from adminTest.common import shiselogo, generate_shiselogoori_name
from adminTest.sscomment.managers import QcommentManager

#一个 ContentType 对象表示django中安装的一个 model
# ContentType 有3个成员：
# app_label，如 jqqmatch
# model，如 Match。app_label 和 model 就唯一决定了一个app中的一个model
# name，该 model 的 Meta class 中设置的 verbose_name，如 "比赛"

#这里用 content_type 表明此 comment 属于哪个 app 中的哪个 model

# ContentType 有2个方法：
# ContentType.get_object_for_this_type(**kwargs)
# ContentType.model_class()

# ContentTypeManager 有3个方法：
# clear_cache()  这个方法基本不会被手工使用，django会自动使用
# get_for_model(model) Takes either a model class or an instance of a model, and returns the ContentType instance representing that model
# get_by_natural_key(app_label, model) Returns the ContentType instance uniquely identified by the given application label and model name

#object_id 表明该model的特定object。结合 content_type 和 object_id，唯一决定了这个comment的主人
#GenericForeignKey 专门处理这个需求。通用外键。


class Qcomment(models.Model):
	content_type 	= models.ForeignKey(ContentType)
	object_id 	= models.CharField(max_length=30)
	content_object 	= generic.GenericForeignKey('content_type', 'object_id')

	author 		= models.ForeignKey(User, verbose_name='作者', related_name='qcomment_author_set')
	content 	= models.TextField('评论内容')
	has_quote 	= models.BooleanField('是否有引用', default=False)
	quote 		= models.TextField('引用内容', blank=True)

	submit_date 	= models.DateTimeField('发表时间', auto_now_add=True)
	is_public   	= models.BooleanField('是否公开',  default=True)
	lights 		= models.IntegerField('点亮数',    default=0)
	lighters	= models.ManyToManyField(User, related_name='qcomment_lighters_set', verbose_name='点亮者', blank=True)
	imgs        = models.ImageField('评论图片',	upload_to=generate_shiselogoori_name, 	blank=True)

	absorption    = models.IntegerField('吸收度',    default=0)
	durability    = models.IntegerField('持久度',    default=0) 
	ppr           = models.IntegerField('性价比',    default=0) 
	color         = models.IntegerField('色彩度',    default=0) 
	anti_blooming = models.IntegerField('防晕染',    default=0) 
	
	objects 	= QcommentManager()
	
	class Meta:
		ordering = ('id', 'content_type', 'submit_date', )
	
	def __unicode__(self):
		return u'[%s] [%s] %s...' %(self.content_object, self.author.username, self.comment[:50])

	def get_author_url(self):
		return u'%s' %(self.author.get_profile().get_absolute_url())
	def get_authorlogo_url(self):
		return u'%s' %(self.author.get_profile().logo.url)

	#判断user是否点亮过这个评论
	def has_lighter(self, user):
		return True if user in self.lighters.all() else False
