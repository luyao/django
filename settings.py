#coding=utf8
# Django settings for adminTest project.
import os.path

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('luyao', '719959733@qq.com'),
)

WORK_DIR=os.path.dirname(os.path.abspath(__file__))

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'adminTest'         # Or path to database file if using sqlite3.
DATABASE_USER = 'root'              # Not used with sqlite3.
DATABASE_PASSWORD = 'lala200403'    # Not used with sqlite3.
DATABASE_HOST = '127.0.0.1'         # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             	    # Set to empty string for default. Not used with sqlite3.


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LlslsNGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'
DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'
LOGIN_REDIRECT_URL = '/'
AUTH_PROFILE_MODULE = 'ssuser.RegistrationProfile'

#AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'jiaoqiqu.jqquser.models.KeyBackend',)
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

SITE_ID = 1

SITE_NAME = "shise.com"
SITE_ADDRESS= '122.200.77.77:1107'
ACCOUNT_ACTIVATION_DAYS = 7 
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

if True:
	EMAIL_USE_TLS = True
	EMAIL_HOST = 'smtp.163.com'
	EMAIL_PORT = '25'
	EMAIL_HOST_USER = 'chinashise@163.com'
	EMAIL_HOST_PASSWORD = '123abc'
	SERVER_EMAIL = EMAIL_HOST_USER
	DEFAULT_FROM_EMAIL  = '试色网<chinashise@163.com>'
	EMAIL_SUBJECT_PREFIX = '[SS] '




# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(WORK_DIR, 'static/img/').replace('\\','/')
MEDIA_SITE_ROOT = '/static/img/'
MEDIA_ROOT_ = 'static/img/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/'

DEFAULT_LOGO_PATH='/static/img/userlogo/50_jqq_user_default.jpg'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/luyao/django/adminTest/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')@+k3um8egr7peuh6qr20trpr+op&tz$vsd*ipr=iv!^wy2ebi'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'adminTest.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'adminTest.sspayment',
    'adminTest.homepageItem',
	'adminTest.ssuser',
	'adminTest.ssitem',
	'adminTest.ssbrand',
	'adminTest.sscomment',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
	    'standard': {
		    'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
		    'datefmt' : "%Y-%m-%d %H:%M:%S"
	    },
    },

    'handlers': {
	'null': {
	    'level': 'DEBUG',
	    'class': 'django.utils.log.NullHandler',
	},
	'logfile': {
		'level':'DEBUG',
		'class':'logging.handlers.RotatingFileHandler',
		'filename': "/home/luyao/django/log/shise.log",
		'maxBytes': 50000,
		'backupCount': 2,
		'formatter': 'standard',
	},
	'console':{
		'level':'INFO',
		'class':'logging.StreamHandler',
		'formatter': 'standard'
	},
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },

    'loggers': {
	'django': {
	    'handlers': ['null'],
	    'propagate': True,
	    'level': 'INFO',
	},
        'django.request': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
	'django.db.backends': {
		'handlers': ['console'],
		'level': 'DEBUG',
		'propagate': False,
	},
	'jqqcomment': {
		'handlers': ['console', 'logfile'],
		'level': 'DEBUG',
	},
    }
}
