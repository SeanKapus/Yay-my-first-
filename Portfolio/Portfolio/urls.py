from django.conf.urls import patterns, include, url

from django.contrib import admin
from mypages.views import about_me

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'mypages.views.home_page', name='home'),
    url(r'^about$', 'mypages.views.about_me' , name='about'),
    # url(r'Life/$', 'brochure.views.life'),
)
