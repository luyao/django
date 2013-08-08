from django.conf import settings
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
from adminTest.sscomment.models import Qcomment
from adminTest.sscomment.forms import QcommentForm
from django.utils.importlib import import_module
DEFAULT_COMMENTS_APP = 'django.contrib.comments'

def get_comment_app():
	comments_app = get_comment_app_name()
	if comments_app not in setting.INSTALLED_APPS:
		raise ImproperlyConfigured("The COMMENTS_APP (%r) must be in INSTALLED_APPS" % settings.COMMENTS_APP)
	try:
		package = import_module(comments_app)
	except ImportError:
		raise ImproperlyConfigured("The COMMENTS_APP setting refers to a non-existing package.")

def get_comment_app_name():
	return getattr(settings, 'COMMENTS_APP')

def get_model():
	return Qcomment

def get_form():
	return QcommentForm

def get_form_target():
	return urlresolvers.reverse("adminTest.sscomment.views.post_comment")
	
