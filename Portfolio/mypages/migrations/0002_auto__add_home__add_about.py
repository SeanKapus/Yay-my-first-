# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Home'
        db.create_table(u'mypages_home', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
        ))
        db.send_create_signal(u'mypages', ['Home'])

        # Adding model 'About'
        db.create_table(u'mypages_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mypages', ['About'])


    def backwards(self, orm):
        # Deleting model 'Home'
        db.delete_table(u'mypages_home')

        # Deleting model 'About'
        db.delete_table(u'mypages_about')


    models = {
        u'mypages.about': {
            'Meta': {'object_name': 'About'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mypages.home': {
            'Meta': {'object_name': 'Home'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        }
    }

    complete_apps = ['mypages']