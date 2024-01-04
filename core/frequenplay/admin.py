from django.contrib import admin
from .models import MultipleChoiceGame, Choice

# Register your models here.
admin.site.register(MultipleChoiceGame)
admin.site.register(Choice)