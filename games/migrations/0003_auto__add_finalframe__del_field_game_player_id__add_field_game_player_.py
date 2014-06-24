# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinalFrame'
        db.create_table('games_finalframe', (
            ('frame_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['games.Frame'], unique=True, primary_key=True)),
            ('fill_ball', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, default=None, null=True)),
        ))
        db.send_create_signal('games', ['FinalFrame'])

        # Deleting field 'Game.player_id'
        db.delete_column('games_game', 'player_id_id')

        # Adding field 'Game.player'
        db.add_column('games_game', 'player',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Player']),
                      keep_default=False)

        # Deleting field 'Frame.fill_ball'
        db.delete_column('games_frame', 'fill_ball')

        # Deleting field 'Frame.order'
        db.delete_column('games_frame', 'order')

        # Adding field 'Frame.frame_number'
        db.add_column('games_frame', 'frame_number',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FinalFrame'
        db.delete_table('games_finalframe')

        # Adding field 'Game.player_id'
        db.add_column('games_game', 'player_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['games.Player']),
                      keep_default=False)

        # Deleting field 'Game.player'
        db.delete_column('games_game', 'player_id')

        # Adding field 'Frame.fill_ball'
        db.add_column('games_frame', 'fill_ball',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, default=None, null=True),
                      keep_default=False)

        # Adding field 'Frame.order'
        db.add_column('games_frame', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Frame.frame_number'
        db.delete_column('games_frame', 'frame_number')


    models = {
        'games.finalframe': {
            'Meta': {'object_name': 'FinalFrame', '_ormbases': ['games.Frame']},
            'fill_ball': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'frame_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['games.Frame']", 'unique': 'True', 'primary_key': 'True'})
        },
        'games.frame': {
            'Meta': {'object_name': 'Frame'},
            'ball_1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ball_2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frame_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'game_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.Game']"}),
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