from django.db import models
import datetime
from django.utils import timezone

class Player(models.Model):
    nickname = models.CharField(max_length=200)
    average = models.IntegerField(default=0)

    def __repr__(self):
        return '<nickname {}>'.format(self.nickname)

class Game(models.Model):
    player_id = models.ForeignKey(Player)
    lane = models.PositiveSmallIntegerField(default=1)
    score = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)
    play_date = models.DateTimeField('date played')
    
    def __repr__(self):
        return '<player_id {}> <lane {}> <score {}>'.format(self.player_id, self.lane, self.score)