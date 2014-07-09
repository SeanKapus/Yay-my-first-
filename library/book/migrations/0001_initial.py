# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table(u'book_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'book', ['BlogPost'])

        # Adding model 'Author'
        db.create_table(u'book_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.BlogPost'])),
        ))
        db.send_create_signal(u'book', ['Author'])

        # Adding model 'Comment'
        db.create_table(u'book_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Author'])),
        ))
        db.send_create_signal(u'book', ['Comment'])

        # Adding model 'Tag'
        db.create_table(u'book_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'book', ['Tag'])

        # Adding M2M table for field tag on 'Tag'
        m2m_table_name = db.shorten_name(u'book_tag_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'book.tag'], null=False)),
            ('comment', models.ForeignKey(orm[u'book.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table(u'book_blogpost')

        # Deleting model 'Author'
        db.delete_table(u'book_author')

        # Deleting model 'Comment'
        db.delete_table(u'book_comment')

        # Deleting model 'Tag'
        db.delete_table(u'book_tag')

        # Removing M2M table for field tag on 'Tag'
        db.delete_table(db.shorten_name(u'book_tag_tag'))


    models = {
        u'book.author': {
            'Meta': {'object_name': 'Author'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.BlogPost']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'book.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'book.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Author']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'book.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['book.Comment']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['book']