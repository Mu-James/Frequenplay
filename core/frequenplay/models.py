from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class User(models.Model):
    uid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        help_text = "Unique User ID."
    )

    username = models.CharField(
        max_length = 25,
        unique = True,
        help_text = "Enter a unique Username."
    )

    email = models.EmailField(
        unique = True,
        help_text = "Enter a unique Email."
    )

    password = models.CharField(
        max_length = 100,
        help_text = "Enter a Password."
    )

    #Might need a Field for User created Games

    def __str__(self):
        return "User: " + self.username + "." + self.uid
    
    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('user-detail', args=[str(self.id)])

class MC_Game(models.Model):
    """Model representing a Game instance."""

    user = models.ForeignKey(User, on_delete = models.RESTRICT, null = True)

    game_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        help_text = "Unique Game ID."
    )

    name = models.CharField(
        max_length = 100,
        unique = True,
        help_text = "Enter a name for your Game."
    )

    youtube_video_url = models.URLField(
        max_length = 200,
        help_text = "Enter the Youtube Video URL for the Game."
    )

    youtube_video_id = models.CharField(
        max_length = 100,
        help_text = "Enter the Youtube Video Id for the Game"
    )

    date_created = models.DateField(
        help_text = "Enter the date of Game creation."
    )

    num_plays = models.IntegerField(
        help_text = "Enter the number of times this Game has been played."
    )

    def __str__(self):
        """String for representing the Game object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('game-detail', args=[str(self.id)])