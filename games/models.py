import datetime
from django.db import models
from model_utils.managers import InheritanceManager
from django.utils import timezone

class Player(models.Model):
    nickname = models.CharField(max_length=200)
    average = models.IntegerField(default=0)

    def __repr__(self):
        return '<nickname {}>'.format(self.nickname)

class Game(models.Model):
    player = models.ForeignKey(Player)
    lane = models.PositiveSmallIntegerField(default=1)
    score = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)
    play_date = models.DateTimeField('date played')

    class Meta:
        ordering = ['-play_date']


    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
            super(Game, self).save(*args, **kwargs)
            for i in range(1,10):
                f = Frame()
                f.game = self
                f.frame_number = i
                f.save()
            ff = FinalFrame()
            ff.game = self
            ff.frame_number = 10
            ff.save()
        super(Game, self).save(*args, **kwargs)
    
    @property
    def current_frame(self):
        return self.frame_set.filter(balls__gt=0)[0]

    def __repr__(self):
        return '<player_id {}> <lane {}> <score {}>'.format(self.player_id, self.lane, self.score)

class Frame(models.Model):
    game = models.ForeignKey(Game)
    frame_number =  models.PositiveSmallIntegerField(default=0)
    closed = models.BooleanField(default=False)
    balls = models.PositiveSmallIntegerField(default=2)
    ball_1 = models.PositiveSmallIntegerField(default=0)
    ball_2 = models.PositiveSmallIntegerField(default=0)
    objects = InheritanceManager()

    class Meta:
        ordering = ['frame_number']

    def count_pins(self, pins):
        c = 0
        for i in range(0,10):
            m = 1 << i
            if pins & m:
                c = c + 1
        return c

    @property
    def partial_score(self):
        next_frame = self.game.frame_set.get_subclass(frame_number=self.frame_number + 1)
        if self.count_pins(self.ball_1) == 10:
            # Strike!
            if next_frame.balls == 0:
                return 10 + next_frame.count_pins(self.ball_1) + next_frame.count_pins(ball_2)
            return None
        elif self.count_pins(self.ball_1 | self.ball_2) == 10:
            # Spare!
            if next_frame.balls == 0:
                return 10 + next_frame.count_pins(self.ball_1)
            return None
        else:
            return  self.count_pins(self.ball_1 | self.ball_2)

    def __str__(self):
        return str(self.frame_number)

class FinalFrame(Frame):
    fill_ball = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

    @property
    def partial_score(self):
        if self.balls == 0:
            return self.count_pins(self.ball_1 + self.count_pins(self.ball_2) + self.count_pins(fill_ball))
        else:
            if self.balls == 2 and self.count_pins(self.ball_1) == 10:
                # Strike!
                return None
            elif self.balls == 1 and self.count_pins(self.ball_1 | self.ball_2) == 10:
                # Spare!
                if next_frame.balls == 0:
                    return 10 + next_frame.count_pins(ball_1)
                return None
            else:
                return  self.count_pins(self.ball_1 | self.ball_2)
    def __str__(self):
        return self.frame_number
