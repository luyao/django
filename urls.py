from django.conf.urls.defaults import *
#activate the static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from adminTest.views import *

#auth
from django.contrib.auth.views import login, logout_then_login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^adminTest/', include('adminTest.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url':settings.MEDIA_URL+'favicon.ico'}),
)

urlpatterns += patterns('',
    (r'^hello/$', hello),
    (r'^addFile/$', addFile),
    (r'^time/(\d{1,2})/$', hour_ahead_ex),
)

urlpatterns += patterns('',
    (r'^scroll/$', scroll_demo),
)


#home page
urlpatterns += patterns('',
    (r'^$', home_index),
)

#for the search
urlpatterns += patterns('',
    #(r'^search/item/(?P<id>[^/]+)$', search_item),
    #(r'^search/user/(?P<id>[^/]+)$', search_user),
    #(r'^search/cate/(?P<id>[^/]+)$', search_cate),
)

#use ajax to transit data
urlpatterns += patterns('',
    (r'^/post/item/(?P<id>[^/]+)/$', post_item),
)


#payment
urlpatterns += patterns('sspayment.views',
	#cart's view
	(r'^cart/view/$', 'cart_view'),
	#add the product
	(r'^cart/add/(?P<id>[^/]+)/$', 'add_to_cart'),  
	#delete one product
	(r'^cart/del/(?P<id>[^/]+)/$', 'del_from_cart'),  
	#clean the cart
	(r'^cart/clean/', 'clean_cart'),
	#pay me!
	(r'^pay/', 'pay'),
)


#
#urlpatterns += patterns('shise.views',

#	(r'^$', 'homeview'),
#
#	(r'^qcomment_highlight/$', 'qcomment_highlight'),
#	(r'^qcomment_delete/$', 'qcomment_delete'),
#
#	(r'^base/$', 'base'),
#	(r'^test/$', 'test'),
#	(r'^about/$', 'about'),
#	(r'^partner/$', 'partner'),
#	(r'^contact/$', 'contact'),
#)
#

urlpatterns += patterns('adminTest.ssitem.views',
	#the page which show single item	
	(r'^shise/(?P<sid>\d+)/$', 'shiseview'),
)

#user
urlpatterns += patterns('adminTest.ssuser.views',
	(r'^accounts/register/$', "register"),
	(r'^accounts/aregister/$', 'register', {'template_name': 'registration/activate_register.html'}),
	(r'^accounts/lregister/$', 'register', {'template_name': 'registration/login_register.html'}),
	(r'^accounts/email/(?P<emailaddress>.*)/$', 'accemail'),
	#(r'^accounts/logo/(?P<activation_key>.*)/$', 'acclogo'),
	(r'^accounts/reemail/(?P<emailaddress>.*)/$', 'accemail'),
	(r'^accounts/key/(?P<activation_key>.*)/$', 'activate'),
	(r'^accounts/agreement/$', 'accagreement'),
	(r'^accounts/login/$', 'emaillogin'),
	(r'^accounts/logout/$', logout_then_login),
	(r'^accounts/alogin/$', 'emaillogin', {'template_name': 'registration/activate_login.html'}),
)

urlpatterns += staticfiles_urlpatterns()  
