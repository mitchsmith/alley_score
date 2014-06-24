# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Frame.game_id'
        db.delete_column('games_frame', 'game_id_id')

        # Adding field 'Frame.game'
        db.add_column('games_frame', 'game',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Game']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Frame.game_id'
        db.add_column('games_frame', 'game_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Game']),
                      keep_default=False)

        # Deleting field 'Frame.game'
        db.delete_column('games_frame', 'game_id')


    models = {
        'games.finalframe': {
            'Meta': {'object_name': 'FinalFrame', '_ormbases': ['games.Frame']},
            'fill_ball': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': 'None'}),
            'frame_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['games.Frame']"})
        },
        'games.frame': {
            'Meta': {'object_name': 'Frame'},
            'ball_1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ball_2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frame_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'games.game': {
            'Meta': {'object_name': 'Game'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'play_date': ('django.db.models.fields.DateTimeField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Player']"}),
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