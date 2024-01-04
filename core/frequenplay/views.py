import sys, os
sys.path.append(os.path.abspath("frequenplay/functions"))

from django.shortcuts import get_object_or_404, render
from .models import MultipleChoiceGame

# Create your views here.
def index(request):
    """View function for home page of site"""
    """Game Selection on index page"""
    num_games = MultipleChoiceGame.objects.all().count()
    game_list = MultipleChoiceGame.objects.order_by("-pub_date")

    context = {
        "num_games" : num_games,
        "game_list" : game_list
    }

    return render(request, 'index.html', context=context)

def game_read(request, game_id):
    MCG = get_object_or_404(MultipleChoiceGame, pk = game_id)

    context = {
        "MCG" : MCG,
        "game_id" : game_id,
    }

    return render(request, "game/read/read.html", context=context)

def game_play(request, game_id):
    MCG = get_object_or_404(MultipleChoiceGame, pk = game_id)

    context = {
        "MCG_name" : MCG.name,
        "youtube_id" : MCG.youtube_video_id,
    }
    return render(request, "game/play/play.html", context=context)

def game_results(request, game_id) :
    return HttpResponse("Game Results View." % game_id)