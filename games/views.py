from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from games.models import Player, Game

class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        """Return games as a list."""
        return Game.objects.order_by('-play_date')

class DetailView(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'


class ResultsView(generic.DetailView):
    model = Game
    template_name = 'games/results.html'

def bowl(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    try:
        frame = game.current_frame
    except (KeyError, Game.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'games/detail.html', {
            'game': game,
            'error_message': "Something went wrong.",
        })
    else:
        pins = request.POST['pins']
        if frame.balls == 2:
            frame.ball_1 = pins
        else:
            frame.ball_2 = pins
        frame.balls = frame.balls - 1 
        frame.save()
        game.save()
        return HttpResponseRedirect(reverse('detail', args=(game.id,)))