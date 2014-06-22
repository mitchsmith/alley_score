# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Frame'
        db.create_table('games_frame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ball_1', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('ball_2', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('fill_ball', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=None)),
        ))
        db.send_create_signal('games', ['Frame'])


    def backwards(self, orm):
        # Deleting model 'Frame'
        db.delete_table('games_frame')


    models = {
        'games.frame': {
            'Meta': {'object_name': 'Frame'},
            'ball_1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ball_2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fill_ball': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': 'None'}),
            'game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
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