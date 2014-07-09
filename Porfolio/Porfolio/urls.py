from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'Porfolio.views.home', name='home'),
# #     # url(r'^blog/', include('blog.urls')),
#
urlpatterns = patterns('',
#     url(r'^hello/$', 'brochure.views.hello'),
# )

#
#     url(r'^admin/', include(admin.site.urls)),
# )

# urlpatterns = patterns('',
#     url(r'^ollo/$', 'brochure.views.ollo'),
#
#     url(r'^admin/', include(admin.site.urls))
# )
# urlpatterns = patterns('',
#     # Variables are captured in the part of the url in parentheses
#     # The '?P<variable_name>' syntax lets you name the variable
#     # The regex after the variable's name indicates what is allowed
#     url(r'^hello/(?P<name>\w+)$', 'brochure.views.hello'),
# )
# urlpatterns = patterns('',
#         url(r'drinks/(?P<var1>\D+)/(?P<var2>\D+)$', 'brochure.views.drinks'),
# )

# url(r'Hello/(?P<name>\w+)/(?P<color>\w+)$', 'brochure.views.hello'),


url(r'Life/$', 'brochure.views.life'),
)
