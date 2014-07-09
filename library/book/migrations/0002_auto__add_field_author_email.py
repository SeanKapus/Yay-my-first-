# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.email'
        db.add_column(u'book_author', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Author.email'
        db.delete_column(u'book_author', 'email')


    models = {
        u'book.author': {
            'Meta': {'object_name': 'Author'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.BlogPost']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True'}),
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