from django.shortcuts import render
from .models import MultipleChoiceGame

# Create your views here.
def index(request):
    """View function for home page of site"""
    num_games = MultipleChoiceGame.objects.all().count()

    context = {
        "num_games" : num_games
    }

    return render(request, 'index.html', context=context)