# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('games_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('average', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('games', ['Player'])

        # Adding model 'Game'
        db.create_table('games_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Player'])),
            ('lane', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('play_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('games', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('games_player')

        # Deleting model 'Game'
        db.delete_table('games_game')


    models = {
        'games.game': {
            'Meta': {'object_name': 'Game'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'play_date': ('django.db.models.fields.DateTimeField', [], {}),
            'player_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Player']"}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'games.player': {
            'Meta': {'object_name': 'Player'},
            'average': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['games']