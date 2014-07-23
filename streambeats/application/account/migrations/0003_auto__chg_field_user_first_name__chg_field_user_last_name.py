# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.first_name'
        db.alter_column(u'account_user', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'User.last_name'
        db.alter_column(u'account_user', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

    def backwards(self, orm):

        # Changing field 'User.first_name'
        db.alter_column(u'account_user', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'User.last_name'
        db.alter_column(u'account_user', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

    models = {
        u'account.user': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['account']