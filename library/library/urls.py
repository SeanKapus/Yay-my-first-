from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'book.views.home', name='home'),

    url(r'^blogs/$', 'book.views.blog', name='blog'),
    url(r'^blogs/new/$', 'book.views.new_blog', name='new_blog'),
    url(r'^blogs/(?P<blog_id>\w+)/$', 'book.views.view_blog', name='view_blog'),
    url(r'^blogs/(?P<blog_id>\w+)/edit/$', 'book.views.edit_blog', name='edit_blog'),
    url(r'^blogs/(?P<blog_id>\w+)/delete/$', 'book.views.delete_blog', name='delete_blog'),

    url(r'^$', 'book.views.my_form_view', name='my_form_view'),
    url(r'^$', 'book.views.comment_form', name='comment_form'),
    url(r'^comment/new/$', 'book.views.new_comment', name='new_comment'),

)
