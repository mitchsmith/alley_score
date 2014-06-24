import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from games.models import Player, Game, Frame, FinalFrame


def create_player(nickname):
    """
    Creates a player object.
    """
    return Player.objects.create(nickname=nickname)

def create_game(player):
    """
    Creates a new game object
    """
    return Game.objects.create(player=player, play_date=timezone.now())

