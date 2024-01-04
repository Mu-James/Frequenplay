from django.urls import path
from . import views

app_name = "frequenplay"
urlpatterns = [
    path('', views.index, name = 'index'),
    path("<game_id>/", views.game_read, name="read"),
    path("<game_id>/results", views.game_results, name="results"),
    path("<game_id>/play", views.game_play, name="play")
]