#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

#定制 Qcomment 的 manager
class QcommentManager(models.Manager):

	def for_model(self, model):
		"""
		QuerySet for all qcomments for a particular model (either an instance or
		a class).
		"""
		#通过 model 得到该 model 的 contenttype object，如通过match得到表示match的contenttype
		ct = ContentType.objects.get_for_model(model)

		#过滤得到特定 contenttype，也就是 model 的所有 comment
		qs = self.get_query_set().filter(content_type=ct)

		if isinstance(model, models.Model):
			#过滤得到特定 object 的所有 comment
			qs = qs.filter(object_pk=force_unicode(model._get_pk_val()))
		return qs
