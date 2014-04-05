# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserAuthorization'
        db.create_table(u'accounts_userauthorization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('authorized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permissions_granted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='permissions_granted_by', null=True, to=orm['auth.User'])),
            ('permission_granted_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 1, 0, 0), auto_now_add=True, blank=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserProfile'])),
        ))
        db.send_create_signal(u'accounts', ['UserAuthorization'])

        # Adding model 'EmailDomain'
        db.create_table(u'accounts_emaildomain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_domain', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Organization'])),
        ))
        db.send_create_signal(u'accounts', ['EmailDomain'])

        # Adding field 'UserProfile.email'
        db.add_column(u'accounts_userprofile', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UserAuthorization'
        db.delete_table(u'accounts_userauthorization')

        # Deleting model 'EmailDomain'
        db.delete_table(u'accounts_emaildomain')

        # Deleting field 'UserProfile.email'
        db.delete_column(u'accounts_userprofile', 'email')


    models = {
        u'accounts.emaildomain': {
            'Meta': {'object_name': 'EmailDomain'},
            'email_domain': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Organization']"})
        },
        u'accounts.organization': {
            'Meta': {'unique_together': "(('name', 'primary_contact'),)", 'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'primary_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'accounts.userauthorization': {
            'Meta': {'object_name': 'UserAuthorization'},
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission_granted_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'permissions_granted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'permissions_granted_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserProfile']"})
        },
        u'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Organization']", 'null': 'True', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']