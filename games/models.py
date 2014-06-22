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

    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
            for i in range(1,11):
                f = games.models.Frame()
                f.game_id = self.game_id
                f.order = i
                f.save()

        super(Game, self).save(*args, **kwargs)
    
    def __repr__(self):
        return '<player_id {}> <lane {}> <score {}>'.format(self.player_id, self.lane, self.score)

class Frame(models.Model):
    game_id = models.ForeignKey(Game)
    order =  models.PositiveSmallIntegerField(default=0)
    closed = models.BooleanField(default=False)
    ball_1 = models.PositiveSmallIntegerField(default=0)
    ball_2 = models.PositiveSmallIntegerField(default=0)
    fill_ball = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
