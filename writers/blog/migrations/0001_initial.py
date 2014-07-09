# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'blog_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
        ))
        db.send_create_signal(u'blog', ['Author'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['blog.Author'])),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding M2M table for field posts on 'Tag'
        m2m_table_name = db.shorten_name(u'blog_tag_posts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'post_id'])

        # Adding model 'User'
        db.create_table(u'blog_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'blog', ['User'])

        # Adding M2M table for field like on 'User'
        m2m_table_name = db.shorten_name(u'blog_user_like')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'blog.user'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'post_id'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_comment', to=orm['blog.User'])),
        ))
        db.send_create_signal(u'blog', ['Comment'])

        # Adding M2M table for field post on 'Comment'
        m2m_table_name = db.shorten_name(u'blog_comment_post')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm[u'blog.comment'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comment_id', 'post_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'blog_author')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Removing M2M table for field posts on 'Tag'
        db.delete_table(db.shorten_name(u'blog_tag_posts'))

        # Deleting model 'User'
        db.delete_table(u'blog_user')

        # Removing M2M table for field like on 'User'
        db.delete_table(db.shorten_name(u'blog_user_like'))

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')

        # Removing M2M table for field post on 'Comment'
        db.delete_table(db.shorten_name(u'blog_comment_post'))


    models = {
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'comments'", 'symmetrical': 'False', 'to': u"orm['blog.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_comment'", 'to': u"orm['blog.User']"})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['blog.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Post']", 'symmetrical': 'False'})
        },
        u'blog.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'like': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes'", 'symmetrical': 'False', 'to': u"orm['blog.Post']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['blog']