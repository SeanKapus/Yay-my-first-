# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'Hollywood_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Hollywood', ['Genre'])

        # Adding model 'Movie'
        db.create_table(u'Hollywood_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Hollywood.Genre'])),
        ))
        db.send_create_signal(u'Hollywood', ['Movie'])

        # Adding model 'Actor'
        db.create_table(u'Hollywood_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'Hollywood', ['Actor'])

        # Adding M2M table for field movies on 'Actor'
        m2m_table_name = db.shorten_name(u'Hollywood_actor_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actor', models.ForeignKey(orm[u'Hollywood.actor'], null=False)),
            ('movie', models.ForeignKey(orm[u'Hollywood.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actor_id', 'movie_id'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'Hollywood_genre')

        # Deleting model 'Movie'
        db.delete_table(u'Hollywood_movie')

        # Deleting model 'Actor'
        db.delete_table(u'Hollywood_actor')

        # Removing M2M table for field movies on 'Actor'
        db.delete_table(db.shorten_name(u'Hollywood_actor_movies'))


    models = {
        u'Hollywood.actor': {
            'Meta': {'object_name': 'Actor'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Hollywood.Movie']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Hollywood.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Hollywood.movie': {
            'Meta': {'object_name': 'Movie'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Hollywood.Genre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['Hollywood']