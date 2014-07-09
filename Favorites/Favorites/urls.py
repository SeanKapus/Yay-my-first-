from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'Hollywood.views.home', name='home'),

    url(r'^genres/$', 'Hollywood.views.genres', name='genres'),
    url(r'^genres/new/$', 'Hollywood.views.new_genre', name='new_genre'),
    url(r'^genres/(?P<genre_id>\w+)/$', 'Hollywood.views.view_genre', name='view_genre'),
    url(r'^genres/(?P<genre_id>\w+)/edit/$', 'Hollywood.views.edit_genre', name='edit_genre'),
    url(r'^genres/(?P<genre_id>\w+)/delete/$', 'Hollywood.views.delete_genre', name='delete_genre'),

    url(r'^movies/$', 'Hollywood.views.movies', name='Movies'),
    url(r'^movies/new/$', 'Hollywood.views.new_movie', name='new_movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'Hollywood.views.movies', name='view_movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'Hollywood.views.edit_movie' , name='edit_movie'),

    url(r'^actors/$', 'Hollywood.views.actor', name='Actor'),
    url(r'^actors/new/$', 'Hollywood.views.new_actor', name='new_actor'),
    url(r'^actor/(?P<actor_id>\w+)/$', 'Hollywood.views.actor', name='view_actor'),

)















