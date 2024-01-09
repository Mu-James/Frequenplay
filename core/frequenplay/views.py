import sys, os
sys.path.append(os.path.abspath("frequenplay/functions"))
import random as r


from django import forms
from django.shortcuts import get_object_or_404, render
from .models import MultipleChoiceGame, Choice
from .forms import ChooseChoice

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
    """Function to show information of a game before playing"""
    MCG = get_object_or_404(MultipleChoiceGame, pk = game_id)

    context = {
        "MCG" : MCG,
        "game_id" : game_id,
    }

    return render(request, "game/read/read.html", context=context)

def game_play(request, game_id):
    """Function to show choices for players to pick and submit"""
    MCG = get_object_or_404(MultipleChoiceGame, pk = game_id)
    MCG_choice_list = Choice.objects.filter(game=MCG)
    #r.shuffle(list(MCG_choice_list))
    MCG_choice_form = ChooseChoice(MCG=MCG)

    context = {
        "MCG_name" : MCG.name,
        "MCG_youtube_id" : MCG.youtube_video_id,
        "MCG_pub_date" : MCG.pub_date,
        "MCG_choice_form" : MCG_choice_form
    }
    return render(request, "game/play/play.html", context=context)

def game_results(request, game_id) :
    """Function to show result of player's choice after submit"""
    context = {
        "result" : result
    }


    return HttpResponse("Game Results View." % game_id)