from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path("<game_id>/", views.game_read, name="read"),
    path("<int:game_id>/results", views.game_results, name="results"),
    path("<int:game_id>/play", views.game_play, name="play")
]