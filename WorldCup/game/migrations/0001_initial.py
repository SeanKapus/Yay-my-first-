# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tournament'
        db.create_table(u'game_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('host_country', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'game', ['Tournament'])

        # Adding model 'Group'
        db.create_table(u'game_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Tournament', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group', to=orm['game.Tournament'])),
        ))
        db.send_create_signal(u'game', ['Group'])

        # Adding model 'Team'
        db.create_table(u'game_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('team_country', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('Group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team', to=orm['game.Group'])),
        ))
        db.send_create_signal(u'game', ['Team'])

        # Adding model 'Player'
        db.create_table(u'game_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Player_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('Forward', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('Midfield', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Defense', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('Team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player', to=orm['game.Team'])),
        ))
        db.send_create_signal(u'game', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Tournament'
        db.delete_table(u'game_tournament')

        # Deleting model 'Group'
        db.delete_table(u'game_group')

        # Deleting model 'Team'
        db.delete_table(u'game_team')

        # Deleting model 'Player'
        db.delete_table(u'game_player')


    models = {
        u'game.group': {
            'Meta': {'object_name': 'Group'},
            'Tournament': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group'", 'to': u"orm['game.Tournament']"}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'game.player': {
            'Defense': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'Forward': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'Meta': {'object_name': 'Player'},
            'Midfield': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Player_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'Team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player'", 'to': u"orm['game.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'game.team': {
            'Group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team'", 'to': u"orm['game.Group']"}),
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_country': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'game.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'host_country': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['game']