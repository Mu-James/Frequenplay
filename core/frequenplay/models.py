import sys, os
sys.path.append(os.path.abspath("frequenplay/functions"))

import frequenplay_game as fg
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

NUM_WRONG_CHOICES = 3

# Create your models here.
class MultipleChoiceGame(models.Model):
    """Model representing a Game instance."""

    user = models.ForeignKey(get_user_model() , on_delete = models.RESTRICT, null = True)

    game_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid1,
        help_text = "Unique Game ID."
    )

    name = models.CharField(
        max_length = 100,
        unique = True,
        help_text = "Enter a name for the Game."
    )

    youtube_video_url = models.URLField(
        max_length = 200,
        help_text = "Enter the Youtube Video URL for the Game."
    )

    youtube_video_id = models.CharField(
        max_length = 100,
        help_text = "Enter the Youtube Video Id for the Game"
    )

    pub_date = models.DateField(
        help_text = "Enter the date of Game creation."
    )

    num_plays = models.IntegerField(
        default = 0,
        help_text = "The number of times this Game has been played."
    )

    def save(self, *args, **kwargs):
        frequenplayGameInstance = fg.frequenplayGameMC(self.youtube_video_url, self.pub_date, self.name)
        frequenplayGameInstance.generate_random_answer_bank(NUM_WRONG_CHOICES)
        frequenplayGameInstanceAnswerBank = frequenplayGameInstance.get_answer_bank()
        for choice in frequenplayGameInstanceAnswerBank:
            c = Choice(game=self, timestamp=choice, answer=frequenplayGameInstanceAnswerBank[choice])
            c.save()
        super(MultipleChoiceGame, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Game object."""
        return self.name + " with Game ID: " + str(self.game_id)
    
    def get_absolute_url(self):
        """Returns the url to access a particular game instance."""
        return reverse('game-detail', args=[str(self.id)])
    
class Choice(models.Model):
    game = models.ForeignKey(MultipleChoiceGame, on_delete = models.CASCADE)

    timestamp = models.DurationField()
    answer = models.BooleanField()

    def __str__(self):
        return f"{'Correct' if self.answer else 'Inccorect'} Timestamp: {self.timestamp} for {self.game}"