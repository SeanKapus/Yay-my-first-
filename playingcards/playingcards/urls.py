from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from cards.views import poker


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cards.views.home', name='home'),
    # url(r'^cards$', 'cards.views.club_cards', name='club_cards'),
    url(r'^cards$', 'cards.views.card_filters', name="card_filters"),
    url(r'^profiles$', 'cards.views.profile', name='profile'),
    url(r'^faq$',  'cards.views.faq', name='faq'),
    url(r'^blackjack$', 'cards.views.blackjack', name='blackjack'),
    url(r'^poker$', 'cards.views.poker', name='poker'),
    url(r'^hearts$', 'cards.views.hearts', name='hearts'),
    url(r'^not_face$', 'cards.views.not_face', name='not_face'),
    url(r'^register/$', 'cards.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^war/$', 'cards.views.war', name='war'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)